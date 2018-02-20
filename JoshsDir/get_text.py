def text_query(file_name, text, str_len):
    output = ""
    flag1 = False
    with open(file_name, encoding='utf8') as infile:
        for line in infile:
            if line.find(text) != -1 or flag1:
                if not flag1 and line.find(text)+str_len < len(line):
                    output += line[line.find(text):line.find(text)+str_len]
                    break
                elif flag1 and str_len<len(line):
                    output += line[0:str_len]
                    break
                elif not flag1:
                    output += line[line.find(text):len(line)]
                    str_len -= len(line) - line.find(text)
                    flag1 = True
                else:
                    output += line[0:len(line)]
                    str_len -= len(line) - line.find(text)
        return output


my_str = text_query("test.txt", "darkness", 500)
print(my_str)