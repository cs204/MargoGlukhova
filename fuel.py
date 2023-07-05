def calculateFuelPercentage(fuelFraction):
    try:
        x, y = map(int, fuelFraction.split('/'))
        if x < 0 or y <= 0 or x > y:
            raise ValueError
        percentage = (x / y) * 100
        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return round(percentage)
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите корректную дробь в формате x/y, где x и y - целые числа, y больше нуля, и x не больше y.")
        return None
    except ZeroDivisionError:
        print("Ошибка деления на ноль. Пожалуйста, убедитесь, что знаменатель (y) в дроби не равен нулю.")
        return None

def main():
    while True:
        fuelFraction = input("Дробь: ")
        percentage = calculateFuelPercentage(fuelFraction)
        if percentage is not None:
            if percentage == 'F':
                print(percentage)
            elif percentage == 'E':
                print(percentage)
            else:
                print("{}%".format(percentage))
            break

if __name__ == "__main__":
    main()