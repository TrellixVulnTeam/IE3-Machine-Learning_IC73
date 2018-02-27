file_name = "./corpi/all_files.txt"
data = open(file_name, 'r').read()
data = data.lower()

count = 0
while count <10:
    for i in data:
        print i
        count++
