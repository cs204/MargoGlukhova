menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}

def main():
    totalCost = 0.0

    while True:
        try:
            dish = input("Блюдо: ")
            if dish.lower() not in menu:
                continue
            totalCost += menu[dish.lower()]
        except EOFError:
            break

    print(f"\nСумма: {totalCost:.2f}")

if __name__ == "__main__":
    main()