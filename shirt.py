import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        print("Слишком мало аргументов в командной строке")
        sys.exit(1)

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    if not is_valid_extension(inputFile) or not is_valid_extension(outputFile):
        print("Ввод и вывод имеют разные расширения")
        sys.exit(1)

    if not os.path.isfile(inputFile):
        print("Файл не существует")
        sys.exit(1)

    shirt = Image.open("shirt.png")
    photo = Image.open(inputFile)

    photo = ImageOps.fit(photo, shirt.size)

    photo.paste(shirt, (0, 0), mask=shirt)

    photo.save(outputFile)

def is_valid_extension(filename):
    validExtensions = ['.jpg', '.jpeg', '.png']
    _, extension = os.path.splitext(filename)
    return extension.lower() in validExtensions

if __name__ == "__main__":
    main()