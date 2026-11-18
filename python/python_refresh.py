"""
DAY 1 — Python interview questions
Write each function yourself below its question, then run:  python day1_python_refresh.py
"""


# Q1. Return the total of only the positive numbers in a list.
#     Function: total_positive(nums)
#     Input:  [3, -1, 4, -5]      Output: 7
#     Input:  [-2, -8]            Output: 0
#     Input:  []                  Output: 0
def total_positive(nums):
    total_positives = 0
    for num in nums:
        if num > 0:
            total_positives += num
    return total_positives

def total_positive(nums):
    return sum(num for num in nums if num > 0)

# Q2. Return a new list with the square of every even number, in the original order.
#     Function: squares_of_evens(nums)
#     Input:  [1, 2, 3, 4]        Output: [4, 16]
#     Input:  [-2, 0, 3]          Output: [4, 0]
#     Input:  []                  Output: []
def squares_of_evens(nums):
    result = []
    for num in nums:
        if num %2 == 0:
            result.append(num * num)
    return result

def squares_of_evens(nums):
    return [num * num for num in nums if num %2 == 0]

# Q3. Count how many times each word appears in a text (case-insensitive).
#     Function: word_frequency(text)
#     Input:  "the cat and The dog"    Output: {"the": 2, "cat": 1, "and": 1, "dog": 1}
#     Input:  "hi hi hi"               Output: {"hi": 3}
#     Input:  ""                       Output: {}
def word_frequency(text):
    result = {}
    text = text.lower()
    text_list = text.split()
    for t in text_list:
        if t not in result:
            result[t] = 1
        else:
            result[t]+=1
    return result


# Q4. Return True if any value appears more than once in a list, else False.
#     Function: has_duplicates(items)
#     Input:  [1, 2, 3, 1]        Output: True
#     Input:  [1, 2, 3]           Output: False
#     Input:  []                  Output: False

def has_duplicates(items):
    if len(set(items)) !=len(items):
        return True
    else:
        return False

def has_duplicates(items):
    return len(set(items)) != len(items)


# Q5. Given (name, score) pairs, return names sorted by score high to low;
#     equal scores sorted by name A to Z.
#     Function: sort_by_score(pairs)
#     Input:  [("ravi", 80), ("anu", 95), ("bala", 80)]   Output: ["anu", "bala", "ravi"]
#     Input:  [("x", 50)]                                 Output: ["x"]
#     Input:  []                                          Output: []

def sort_by_score(pairs):
    sorted_pairs = sorted(pairs, key = lambda x:(-x[1],x[0]))
    names = []
    for name, score in sorted_pairs:
        names.append(name)
    return names


# Q6. Swap the keys and values of a dictionary (values are unique).
#     Function: invert_dict(d)
#     Input:  {"a": 1, "b": 2}    Output: {1: "a", 2: "b"}
#     Input:  {}                  Output: {}
def invert_dict(d):
    new_dict ={}
    for key, value in d.items():
        new_dict[value] = key
    return new_dict


# Q7. Turn a list of lists into one flat list, keeping order.
#     Function: flatten(list_of_lists)
#     Input:  [[1, 2], [3], []]          Output: [1, 2, 3]
#     Input:  [["c1", "c2"], ["c3"]]     Output: ["c1", "c2", "c3"]
#     Input:  []                         Output: []

def flatten(list_of_lists):
    result = []
    for sublist in list_of_lists:
        for item in sublist:
            result.append(item)
    return result 

# Q8. Return the average of any number of numbers passed as separate arguments;
#     0 if none are passed.
#     Function: average(...)
#     Input:  average(2, 4, 6)    Output: 4.0
#     Input:  average(10)         Output: 10.0
#     Input:  average()           Output: 0
def average(*nums):
    if len(nums) == 0:
        return 0
    return sum(nums)/len(nums)

# Q9. Build a log line from a model name and any number of named settings,
#     in the order given.
#     Function: describe_model(name, ...)
#     Input:  describe_model("llama", temperature=0.2, top_p=0.9)
#     Output: "Model llama | temperature=0.2, top_p=0.9"
#     Input:  describe_model("gpt", max_tokens=100)
#     Output: "Model gpt | max_tokens=100"
#     Input:  describe_model("llama")
#     Output: "Model llama | no settings"
def describe_model(name, **kwargs):
    if not kwargs:
        return f"Model {name} | no settings"
    settings = ", ".join(f"{k}= {v}" for k, v in kwargs.items())
    return f"Model {name} | {settings}"


# Q10. Combine two dictionaries of counts by adding values for the same key.
#      The two input dictionaries must stay unchanged.
#      Function: merge_counts(a, b)
#      Input:  {"x": 1, "y": 2}, {"y": 3, "z": 4}    Output: {"x": 1, "y": 5, "z": 4}
#      Input:  {}, {"a": 1}                          Output: {"a": 1}
#      Input:  {}, {}                                Output: {}
def merge_counts(a,b):
    result = {}
    for k,v in a.items():
        result[k] = v

    for k, v in b.items():
        if k in result:
            result[k] = result[k] + v
        else:
            result[k] = v
    return result


    






# ---------------------------------------------------------------- self-check (don't edit)
def _check():
    g = globals()
    def call(fname, *a, **k):
        return g[fname](*a, **k)
    tests = [
        ("Q1 total_positive", lambda: call("total_positive", [3, -1, 4, -5]) == 7 and call("total_positive", [-2, -8]) == 0 and call("total_positive", []) == 0),
        ("Q2 squares_of_evens", lambda: call("squares_of_evens", [1, 2, 3, 4]) == [4, 16] and call("squares_of_evens", [-2, 0, 3]) == [4, 0] and call("squares_of_evens", []) == []),
        ("Q3 word_frequency", lambda: call("word_frequency", "the cat and The dog") == {"the": 2, "cat": 1, "and": 1, "dog": 1} and call("word_frequency", "hi hi hi") == {"hi": 3} and call("word_frequency", "") == {}),
        ("Q4 has_duplicates", lambda: call("has_duplicates", [1, 2, 3, 1]) is True and call("has_duplicates", [1, 2, 3]) is False and call("has_duplicates", []) is False),
        ("Q5 sort_by_score", lambda: call("sort_by_score", [("ravi", 80), ("anu", 95), ("bala", 80)]) == ["anu", "bala", "ravi"] and call("sort_by_score", [("x", 50)]) == ["x"] and call("sort_by_score", []) == []),
        ("Q6 invert_dict", lambda: call("invert_dict", {"a": 1, "b": 2}) == {1: "a", 2: "b"} and call("invert_dict", {}) == {}),
        ("Q7 flatten", lambda: call("flatten", [[1, 2], [3], []]) == [1, 2, 3] and call("flatten", [["c1", "c2"], ["c3"]]) == ["c1", "c2", "c3"] and call("flatten", []) == []),
        ("Q8 average", lambda: call("average", 2, 4, 6) == 4.0 and call("average", 10) == 10.0 and call("average") == 0),
        ("Q9 describe_model", lambda: call("describe_model", "llama", temperature=0.2, top_p=0.9) == "Model llama | temperature=0.2, top_p=0.9"
                                      and call("describe_model", "gpt", max_tokens=100) == "Model gpt | max_tokens=100"
                                      and call("describe_model", "llama") == "Model llama | no settings"),
        ("Q10 merge_counts", lambda: _merge_ok(call)),
    ]
    passed = 0
    for name, fn in tests:
        try:
            ok = bool(fn())
        except KeyError:
            ok = False
            name += "  (not written yet)"
        except Exception as e:
            ok = False
            name += f"  (error: {type(e).__name__}: {e})"
        print(("PASS  " if ok else "FAIL  ") + name)
        passed += ok
    print(f"\n{passed}/{len(tests)} passed")


def _merge_ok(call):
    a, b = {"x": 1, "y": 2}, {"y": 3, "z": 4}
    out = call("merge_counts", a, b)
    return (out == {"x": 1, "y": 5, "z": 4} and a == {"x": 1, "y": 2} and b == {"y": 3, "z": 4}
            and call("merge_counts", {}, {"a": 1}) == {"a": 1} and call("merge_counts", {}, {}) == {})


if __name__ == "__main__":
    _check()