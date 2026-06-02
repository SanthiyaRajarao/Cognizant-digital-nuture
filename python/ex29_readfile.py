def read_file():
    file = open("message.txt", "r")
    content = file.read()
    file.close()
    print("File Content:")
    print(content)

read_file()