from fandom import set_wiki, search, page

def extract_fanwiki_data(character_name, output_file, min_word_limit=500, max_word_limit=1000):
    # Set the wiki to the Jojo fandom wiki
    set_wiki("Jojo")

    #Search for the character's page
    search_result = search(character_name)
    
    print(f"Search results for '{character_name}': {search_result}")

    #Check if search results are found
    if search_result:
        content = ''
        #Try to gather content from multiple relevant pages
        for title, _ in search_result[:3]:  
            character_page = page(title)
            if isinstance(character_page.content, dict):
                for section, text in character_page.content.items():
                    if isinstance(text, str):
                        content += text + '\n\n'
            else:
                content += character_page.content + '\n\n'
            
            #Stop when it has collect enough content
            if len(content.split()) >= min_word_limit:
                break
        
        #For check the final length of the extracted content
        words = content.split()
        if len(words) < min_word_limit:
            print(f"Extracted content is still below the minimum word count of {min_word_limit} words.")
        else:
            #Limit the content to the specified max word limit
            limited_content = ' '.join(words[:max_word_limit])

            with open(output_file, 'w') as f:
                f.write(limited_content)
        
            actual_word_count = len(limited_content.split())
            print(f"Extracted approximately {actual_word_count} words for '{character_name}' and saved to {output_file}")
    else:
        print(f"Character '{character_name}' not found in Jojo wiki.")

#Replace 'Jotaro Kujo' with the character (my student id 47817283 , "3" is Jotaro Kujo)
extract_fanwiki_data('Jotaro Kujo', 'fanwiki.txt')
