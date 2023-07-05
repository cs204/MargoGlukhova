def getCalories():
    fruitCalories = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20
    }

    fruit = input("Фрукт: ")

    if fruit in fruitCalories:
        calories = fruitCalories[fruit]
        print(f"Калории: {calories}")

def main():
    getCalories()

if __name__ == "__main__":
    main()