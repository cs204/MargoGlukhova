import sys

def countLines(filename):
    try:
        if not filename.endswith('.py'):
            raise ValueError("Не python файл")

        with open(filename, 'r') as file:
            lines = file.readlines()

        count = 0
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                count += 1

        return count

    except FileNotFoundError:
        print("Файл не существует.")
        sys.exit(1)

    except ValueError as e:
        print(e)
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Слишком мало аргументов в командной строке.")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Слишком много аргументов в командной строке.")
        sys.exit(1)

    filenames = sys.argv[1:]
    totalLines = 0

    for filename in filenames:
        linesCount = countLines(filename)
        totalLines += linesCount

    print(totalLines)

if __name__ == '__main__':
    main()