import re

# Function to correct NER tags for punctuation
def fix_ner_tags(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Define a pattern to detect standalone punctuation marks (excluding hyphens within words)
    punctuation_pattern = re.compile(r'^[\.,!?;:"\'()]+$')

    corrected_lines = []

    for line in lines:
        # Skip empty lines
        if not line.strip():
            corrected_lines.append(line.strip())
            continue

        # Split line into word and tag
        parts = line.strip().split()
        if len(parts) == 2:
            word, ner_tag = parts[0], parts[1]

            # Check if the word is standalone punctuation and not already tagged as 'O'
            if punctuation_pattern.match(word) and ner_tag != 'O':
                parts[1] = 'O'  # Correct the tag to 'O'
            
            # Special handling for dashes/hyphens
            if word == '-' and ner_tag == 'O':
                parts[1] = 'O'  # Keep dash as 'O' if it's a standalone punctuation
            corrected_lines.append('\t'.join(parts))
        else:
            # If the line doesn't match expected format, keep it unchanged
            corrected_lines.append(line.strip())

    # Write the corrected content to a new file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(corrected_lines))

    print("Punctuation tags corrected and saved to", output_path)

# Apply the script to your text
fix_ner_tags('standard-wikipedia-training.txt', 'standard-wikipedia-training-corrected.txt')
fix_ner_tags('standard-fanwiki-training.txt', 'standard-fanwiki-training-corrected.txt')

print("Punctuation tags corrected and saved to new files.")
