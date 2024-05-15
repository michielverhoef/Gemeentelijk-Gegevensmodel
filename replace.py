import argparse
import re
import json

def replace_in_file(file_path, replacements):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for search_pattern, replacement in replacements.items():
        content = re.sub(search_pattern, replacement, content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    parser = argparse.ArgumentParser(description="Zoek en vervang meerdere termen in een bestand op basis van een dictionary van patronen en vervangingen.")
    parser.add_argument("file_path", type=str, help="Het pad naar het bestand waarin je wilt zoeken en vervangen.")
    parser.add_argument("replacements_json", type=str, help="Een JSON-string die de dictionary van zoek-en-vervang-paren bevat.")
    
    args = parser.parse_args()
    
    # Convert the JSON string into a dictionary
    replacements = json.loads(args.replacements_json)
    
    replace_in_file(args.file_path, replacements)

if __name__ == "__main__":
    main()
