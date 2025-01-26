import numpy as np
"""
Řešení soustavy rovnic:
https://www.wolframalpha.com/calculators/system-equation-calculator

x−y  = 0
3x−y = 1
"""
a1 = np.array([[1, -1], [3, -1]])
a2 = np.array([0, 1])

"""
2x + 3y = 6
4x + 9y = 15

Řešení:
(x,y) = (3/2, 1)
"""
b1 =np.array([
        [2, 3],
        [4, 9]
    ])
b2 = np.array(
    [6, 15]
)

"""
3x + 2y - z = 1
2x + 2y + 4z = -2
-x + 0.5 y - z  =0

Řešení:
(x,y,z) = (1,-2,-2)
"""
c1 = np.array([
        [3, 2, -1],
        [2, 2, 4],
        [-1, 0.5, -1]
    ])
c2 = np.array([1, -2, 0])

# Výpočet řešení soustavy

solution = np.linalg.solve(a1, a2)
s1 = np.linalg.solve(b1, b2)
s2 = np.linalg.solve(c1, c2)

print(s1)
print(s2)

# Výsledek
x, y = solution
print(f"x = {x}, y = {y}")
