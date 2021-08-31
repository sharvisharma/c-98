def count_words_From_File():
    fileName =  input("stort.txt")

    numberOfWords = 0

    file =  open(fileName, 'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of words:")
    print(numberOfWords)


count_words_From_File()
