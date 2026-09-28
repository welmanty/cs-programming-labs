distance = float(input())
liters_100_km = float(input())
price_1_liter = float(input())
liters = distance / 100 * liters_100_km
price = liters * price_1_liter
print(f'Топливо: {liters:.02f} л')
print(f'Стоимость: {price:.02f} руб')
