import math

def log_base_7(x):
    return math.log(x) / math.log(7)

def f(x):
    if x >= 1:
        return 7 * math.log(x) + log_base_7(x) + math.log10(x)
    elif -10.3 < x < 1:
        return math.sin(x) - math.cos(x + 2 + math.pi * 7)
    elif x <= -10.3:
        return 2.24 * math.exp(0.5 * x + 0.1) + 2 ** (0.3 * x)
    else:
        return "Недійсне значення x"

x = float(input("Введіть значення x: "))

result = f(x)
print(f"Значення функції f(x) при x = {x} дорівнює: {result}")
