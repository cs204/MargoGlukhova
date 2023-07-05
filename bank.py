def main():
    userInput = input("Приветствие: ")

    if userInput.lower().startswith("здравствуйте"):
        print("$0")
    elif userInput.lower().startswith("з"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()