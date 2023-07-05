import emoji

def emojizeString(s):
    emojizedOutput = emoji.emojize(s)
    return emojizedOutput

def main():
    userInput = input("Input: ")
    emojizedOutput = emojizeString(userInput)
    print(f"Output: {emojizedOutput}")

if __name__ == "__main__":
    main()