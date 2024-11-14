import re
import sys
import textwrap     
def parse_entries(text):
    entries = re.split(r'#+', text)
    entry_dict = {}
    for entry in entries:
        match = re.search(r'(.*)\n\s*---\n(\s*.+)\n?', 
                          entry, re.DOTALL)
        if match:
            name = match.group(1).strip()
            description = match.group(2).strip()
            entry_dict[name] = description
    return entry_dict

def search(entry_dict, query):
    for script_name, info in entry_dict.items():
        if query.lower() in script_name.lower():
            print(f'Script: {script_name}')
            print('-' * 30 )
            wrapped_info = textwrap.fill(info, width=60)
            print(wrapped_info, "\n")
            print('#' * 30 +'\n')
    return None

if __name__ == "__main__":
    
    title = """
  _  _     ___ ___   _   ___  ___ _  _ 
 | \| |___/ __| __| /_\ | _ \/ __| || |
 | .` |___\__ \ _| / _ \|   / (__| __ |
 |_|\_|   |___/___/_/ \_\_|_\\\\___|_||_|
 ######################################
 """
                                       
                                                  
    print(title)
    no = re.compile(r'[Nn][Oo]?')
    with open('/home/mothballs/Scripts/python/nse_scripts', 'r') as file:
        text = file.read()
        entries = parse_entries(text)
    
    searching = True
    while searching:
        try:
            query = input("Enter search term: ")
        except KeyboardInterrupt:
            exit()
        else:    
            print()
            search(entries, query)
        again = input("Would you like to search again? ")
        if no.match(again):
            searching = False





