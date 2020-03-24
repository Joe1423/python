file_path = 'sample.txt'

with open(file_path) as file_object:
    #with the read() method the content is available only inside the 'with' block
    content = file_object.read()
    print(content)
    print(type(content))

    #check a document line by line
    # for line in file_object:
    #   print(line)

    #you can delete the extra spaces added by default with rstrip()
