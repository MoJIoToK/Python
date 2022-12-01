"""
2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    С помощью математических формул нахождения корней квадратного уравнения

solve(a,b,c)
"""

equation_list = []
for i in input("Введите параметры уравнения: ").split():
    equation_list.append(int(i))

def solve(a, b, c):
    roots = []
    A1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    A2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    if A1 != A2:
        roots.append(A1)
        roots.append(A2)
    else:
        roots.append(A1)
    return roots

print(solve(*equation_list))

