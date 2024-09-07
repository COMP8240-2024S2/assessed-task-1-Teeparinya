import wikipediaapi

def extract_wikipedia_article(title, output_file):
    
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent='TestAssignmentBot/1.0 (https://github.com/COMP8240-2024S2/assessed-task-1-Teeparinya.git)'
    )
    
    page = wiki_wiki.page(title)
    
    #Check if the page exists and write its content to the output file
    if page.exists():
        with open(output_file, 'w') as f:
            f.write(page.text)
        print(f"Extracted {len(page.text)} characters from Wikipedia article '{title}'")
    else:
        print(f"Page '{title}' does not exist")

#Extract the article for 'Tom Cruise'
extract_wikipedia_article('Tom Cruise', 'wikipedia.txt')
