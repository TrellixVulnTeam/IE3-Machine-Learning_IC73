


numbers = ['0','1','2','3','4','5','6','7','8','9']
all_lines = []

with open("all_files.txt", 'r') as fil :
    for line in fil :
        if not(line[0] in numbers):
            all_lines.append(line)


with open("parsed_text.txt",'w') as out:
    for line in all_lines:
        out.write(line)
