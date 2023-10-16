
name = str(input("Cuál es tu nombre?: "))
sales = float(input("Cuánto vendiste en total este mes?: $"))

commissions = round(sales * 13 / 100, 2)

print(f"Ok, {name}. Este mes ganaste ${commissions} de comisiones.")