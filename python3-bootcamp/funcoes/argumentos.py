def somar_todos(*valores):
    total = 0
    for v in valores:
        total += v
    return total

print(somar_todos(1, 2, 3, 4))
