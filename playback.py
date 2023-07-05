def replaceSpacesWithDots(inputString):
    return inputString.replace(" ", "...")

def main():
    userInput = input()
    result = replaceSpacesWithDots(userInput)
    print(result)

if __name__ == "__main__":
    main()