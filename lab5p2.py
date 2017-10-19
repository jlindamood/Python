def main():

    words = []
    while True:

        word = str(input("Enter a list of strings: "))
        if word == "":
            break

        if word[0] in word[1:]:
            words.append(word)

    for x in range(len(words)):
        print(words[x])

main()
