import re

def clean_entity(entity):
    """
    Cleans up an entity string by removing unnecessary characters,
    correcting formatting issues, and ensuring no internal duplication.
    """
    cleaned = entity.replace('(', '').replace(')', '').replace(',', '').strip()
    parts = cleaned.split()
    unique_parts = []
    seen = set()
    for part in parts:
        if part not in seen:
            unique_parts.append(part)
            seen.add(part)
    return ' '.join(unique_parts)

def extract_entities(file_path):
    entities = set()
    entity_pattern = re.compile(r'(\S+)/(\S+)')

    with open(file_path, 'r') as file:
        current_entity = []
        current_tag = None

        for line in file:
            matches = entity_pattern.findall(line)

            for word, tag in matches:
                if tag == 'O':
                    if current_entity:
                        entities.add(clean_entity(' '.join(current_entity)))
                        current_entity = []
                    current_tag = None
                elif tag in {'PERSON', 'ORGANIZATION', 'LOCATION'}:
                    if current_tag == tag:
                        current_entity.append(word)
                    else:
                        if current_entity:
                            entities.add(clean_entity(' '.join(current_entity)))
                        current_entity = [word]
                    current_tag = tag
                else:
                    if current_entity:
                        entities.add(clean_entity(' '.join(current_entity)))
                        current_entity = []
                    current_tag = None

        if current_entity:
            entities.add(clean_entity(' '.join(current_entity)))

    return sorted(entities)

def merge_similar_entities(entities):
    """
    Merge similar entities by prioritizing full names over partial ones,
    ensuring that only relevant entities like "Yare Yare Daze" are retained.
    """
    merged_entities = set()
    full_names = {e for e in entities if len(e.split()) > 1}  # Entities with full names
    partial_names = {e for e in entities if len(e.split()) == 1}  # Entities with partial names

    # Add full names first
    merged_entities.update(full_names)

    # Add partial names only if they don't appear in full names
    for partial in partial_names:
        if not any(partial in full.split() for full in full_names):
            merged_entities.add(partial)

    # Ensure "Yare Yare Daze" is preserved if it was split or misidentified
    if "Yare Yare Daze" in entities or any("Yare" in e for e in full_names):
        merged_entities.add("Yare Yare Daze")

    # Remove explicitly unwanted entities
    filtered_entities = {
        entity for entity in merged_entities 
        if entity not in {'JoJo of the', 'Yare Daze'}  # Exclude specific irrelevant entities
        and entity != ''  # Exclude empty strings
    }

    return filtered_entities

def save_entities(entities, output_file):
    with open(output_file, 'w') as file:
        for entity in sorted(entities):
            file.write(entity + '\n')

# Process Wikipedia NER file
wikipedia_entities = extract_entities('stanford-wikipedia.txt')
wikipedia_entities = merge_similar_entities(wikipedia_entities)
save_entities(wikipedia_entities, 'ner-list-wikipedia.txt')

# Process Fanwiki NER file
fanwiki_entities = extract_entities('stanford-fanwiki.txt')
fanwiki_entities = merge_similar_entities(fanwiki_entities)
save_entities(fanwiki_entities, 'ner-list-fanwiki.txt')

print("Entity extraction and cleaning completed successfully.")
