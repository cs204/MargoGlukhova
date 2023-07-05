def main():
    userInput = input("Приветствие: ")
    result = value(userInput)
    print(f"${result}")

def value(greeting):
    if greeting.lower().startswith("здравствуйте"):
        return 0
    elif greeting.lower().startswith("з"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()