from fandom import set_wiki, search, page
	
def extract_fanwiki_data(character_name, output_file):
	    #Set default Jojo
	    set_wiki("Jojo")
	
	    search_result = search(character_name)
	    
	    #Show search results to help find the correct page
	    print(f"Search results for '{character_name}': {search_result}")
	
	    # Check if search results are found
	    if search_result:
	        #Extract the title from the first search result tuple
	        character_title = search_result[0][0]
	        
	        character_page = page(character_title)
	        
	        #Check if the content is a string or a dictionary and extract the main text
	        if isinstance(character_page.content, dict):
	            content = character_page.content.get('content', '')  
	        else:
	            content = character_page.content
	        	        
	        with open(output_file, 'w') as f:
	            f.write(content)
	        
	        print(f"Extracted data for '{character_title}' and saved to {output_file}")
	    else:
	        print(f"Character '{character_name}' not found in Jojo wiki.")
	
# 'Jotaro Kujo' is match with my student number(47817283)
extract_fanwiki_data('Jotaro Kujo', 'fanwiki.txt')

