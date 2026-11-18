# Q1 — zip + dict comprehension
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [82, 45, 91, 38, 76]
# expected: {"Alice": 82, "Charlie": 91, "Eve": 76}
result = {k:v for k,v in zip(names, scores) if v >=50}
print(result)


# Q2 — lambda + sorted + filter
employees = [
    ("Alice", "Engineering", 95000),
    ("Bob", "Marketing", 72000),
    ("Charlie", "Engineering", 88000),
    ("Diana", "Engineering", 102000),
    ("Eve", "Marketing", 68000),
]
# expected: ["Diana", "Alice", "Charlie"]
filtered = sorted([x for x in employees if x[1]== "Engineering"], key = lambda x: x[2], reverse = True)
result = [x[0] for x in filtered]
print(result)


#Q3 — generator expression (the memory one)
data = range(10_000_000)

# Way 1 — list comprehension
result1 = sum([x*x for x in data if x%2!=0 ])

# Way 2 — generator expression
result2 = sum(x*x for x in data if x %2!=0)

# both result1 and result2 should print the same number
print(result1)
print(result2)

# which one would crash on a real 10M file and why?
# answer: list comprehension