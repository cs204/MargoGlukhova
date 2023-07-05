def camelToSnake(camelCase):
    snakeCase = ""
    for char in camelCase:
        if char.isupper():
            snakeCase += "_" + char.lower()
        else:
            snakeCase += char
    return snakeCase

def main():
    variableName = input("Верблюжий стиль: ")
    snakeCaseName = camelToSnake(variableName)
    print(snakeCaseName)

if __name__ == "__main__":
    main()