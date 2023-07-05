months = ["январь", "февраль", "март", "апрель",
          "май", "июнь", "июль", "август", "сентябрь", "октябрь",
          "ноябрь", "декабрь"]

def main():
    while True:
        userInput = input("Дата: ")

        if "." in userInput:
            parts = userInput.split(".")
        else:
            parts = userInput.split()

        if len(parts) == 3:
            day = parts[0]
            month = parts[1]
            year = parts[2]

            if day.isdigit() and year.isdigit() and (month.isdigit() and 1 <= int(month) <= 12 or month.lower() in months):
                if month.isdigit():
                    month = str(int(month)).zfill(2)
                else:
                    month = str(months.index(month.lower()) + 1).zfill(2)

                day = day.zfill(2)  # Добавляем ведущий ноль, если день однозначный

                isoDate = f"{year}-{month}-{day}"
                print(isoDate)
                break

if __name__ == "__main__":
    main()