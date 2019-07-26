def count_words(file_name):
    '''count words in a file '''
    try:
        with open(file_name) as f:
            contents = f.read()
    except FileNotFoundError:
        # message = "sorry, the file " + file_name + " does not exit."
        # print(message)
        # 这里也可以通过 pass 直接忽略
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) + " words.")


file_name = "fileNotFoundErr.py"
count_words(file_name)

file_name = "fileNotFoundErr_1.py"
count_words(file_name)

file_names = ["Life Stories for Young People.txt","The Shetland Pony by A. I. Douglas and Charles Douglas.txt"]
for file_name in file_names:
    count_words(file_name)