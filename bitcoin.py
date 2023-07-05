import requests
import sys

def main():
    try:
        n = float(sys.argv[1])
    except IndexError:
        print("Пропущен аргумент командной строки")
        sys.exit(1)
    except ValueError:
        print("Аргумент командной строки не число")
        sys.exit(1)

    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()

        usdPrice = data['bpi']['USD']['rate_float']

        totalUsd = n * usdPrice

        formattedUsd = "{:,.4f}".format(totalUsd)
        print("${}".format(formattedUsd))
    except requests.RequestException:
        print("Ошибка при обращении к API CoinDesk Bitcoin Price Index.")
        sys.exit(1)

if __name__ == "__main__":
    main()