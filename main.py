import os
os.environ['PYTHONIOENCODING'] = 'utf-8'

def convert():
    rates = {
        "UAH": 1.0,
        "USD": 41.5,
        "EUR": 43.0,
        "GBP": 51.0
    }

    amount_str = os.getenv("AMOUNT", "1000")
    from_curr = os.getenv("FROM_CURR", "UAH").upper()
    to_curr = os.getenv("TO_CURR", "USD").upper()

    try:
        amount = float(amount_str)
    except ValueError:
        print("Помилка: Некоректна сума!")
        return

    if from_curr not in rates or to_curr not in rates:
        print(f"Помилка: Невідома валюта. Доступні: {list(rates.keys())}")
        return

    amount_in_uah = amount * rates[from_curr]
    result = amount_in_uah / rates[to_curr]

    print("=" * 40)
    print("       КОНВЕРТЕР ВАЛЮТ (Docker)        ")
    print("=" * 40)
    print(f"Початкова сума: {amount} {from_curr}")
    print(f"Результат:      {result:.2f} {to_curr}")
    print("-" * 40)
    print("Доступні курси (до UAH):")
    for curr, rate in rates.items():
        print(f"  1 {curr} = {rate} UAH")
    print("=" * 40)

if __name__ == "__main__":
    convert()