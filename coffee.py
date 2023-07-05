def main():
    amountDue = 50
    changeOwed = 0

    while changeOwed < amountDue:
        print(f"Нужная сумма: {amountDue - changeOwed}")
        coin = input("Вставьте монету: ")

        if coin not in ["50", "20", "10", "5"]:
            continue

        coinValue = int(coin)
        changeOwed += coinValue

    changeOwed -= amountDue
    print(f"Ваша сдача: {changeOwed}")


if __name__ == "__main__":
    main()