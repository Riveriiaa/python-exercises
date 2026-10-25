import math

def calculate_unit_price(diameter_cm, price_euros):
    radius_m = (diameter_cm / 2) / 100
    area = math.pi * radius_m * radius_m
    return price_euros / area

d1 = float(input("Enter the diameter of the first pizza (cm): "))
p1 = float(input("Enter the price of the first pizza (euros): "))

d2 = float(input("Enter the diameter of the second pizza (cm): "))
p2 = float(input("Enter the price of the second pizza (euros): "))

unit_price_1 = calculate_unit_price(d1, p1)
unit_price_2 = calculate_unit_price(d2, p2)

print(f"Unit price of the first pizza: {unit_price_1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unit_price_2:.2f} euros/m²")

if math.isclose(unit_price_1, unit_price_2, rel_tol=1e-9):
    print("Both pizzas provide the same value for money.")
elif unit_price_1 < unit_price_2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")
