def main():
    userInput = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")

    if userInput.lower() == "42" or userInput.lower() == "сорок два":
        print("Да")
    else:
        print("Нет")

if __name__ == "__main__":
    main()