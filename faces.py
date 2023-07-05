def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    userInput = input()
    convertedText = convert(userInput)
    print(convertedText)

if __name__ == "__main__":
    main()