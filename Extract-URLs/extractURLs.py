import re
file_path = input("Enter full path to input file:")

with open(file_path, "r", encoding="utf-8") as file:
    all_lines = file.readlines()  # This reads all lines into a list

all_urls = "".join(all_lines)
urls = re.findall(r'https?://[^\s]+', all_urls)
urls_text = "\n".join(urls)
output_file_path = file_path.rstrip('.txt') + "-extracted.txt"

with open(output_file_path, 'w') as file:
    file.write(urls_text)

print("Done!")