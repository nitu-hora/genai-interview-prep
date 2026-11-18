celsius = [0, 20, 37, 100, -10]
# expected: [32.0, 68.0, 98.6, 212.0, 14.0]
# formula: F = (C × 9/5) + 32

result = list(map(lambda x: (x*9/5) + 32, celsius))
print(result)

words = ["apple", "dog", "elephant", "cat", "owl", "umbrella", "ant", "ice"]
# expected: ["apple", "elephant", "umbrella"]

result = list(filter(lambda x: len(x)>3 and x[0] in "aeiou", words))
print(result)


products = [
    ("Laptop", 80000, 4.5),
    ("Phone", 40000, 4.8),
    ("Tablet", 30000, 4.5),
    ("Earbuds", 5000, 4.8),
]
# expected: [("Earbuds", 5000, 4.8), ("Phone", 40000, 4.8), ("Tablet", 30000, 4.5), ("Laptop", 80000, 4.5)]
result = sorted(products, key = lambda x: (-x[2], x[1]))
print(result)