car_cc = {"mustang": 4951, "aventador": 6498, "chiron": 7993}

max_key = max(car_cc, key=car_cc.get)

print(max_key)