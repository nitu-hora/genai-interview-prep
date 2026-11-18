# ===== SECTION 1: In-place List Modification =====
# Rule: modify the ORIGINAL list using nums[:] = ...
# Wrong way: nums = [...] (creates new list, original unchanged)
# Right way: nums[:] = [...] (replaces contents of original)

def remove_negatives(nums):
    # Input:  [1, -2, 3, -4, 5]
    # Output: nums becomes [1, 3, 5]
    nums[:]= [num for num in nums if num >= 0]

def remove_dupes(nums):
    # Input:  [1, 2, 2, 3, 3, 4]
    # Output: nums becomes [1, 2, 3, 4]  (keep original order)
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    nums[:] = result

def double_evens(nums):
    # Input:  [1, 2, 3, 4, 5]
    # Output: nums becomes [1, 4, 3, 8, 5]  (only even numbers doubled)
    nums[:] = [num*2 if num %2 == 0 else num for num in nums]

 
# ===== SECTION 2: *args and **kwargs =====
# *args   → collects positional args into a TUPLE
# **kwargs → collects keyword args into a DICT

def average(*args):
    # Input:  average(1, 2, 3)
    # Output: 2.0
    # Input:  average(10, 20)
    # Output: 15.0
    # Rule: sum of all args divided by count
    return (sum(args)/len(args))

def introduce(name, **kwargs):
    # Input:  introduce("Nitu", age=25, city="Pune")
    # Output: prints → Name: Nitu | age=25 | city=Pune
    # Input:  introduce("Raj", role="engineer")
    # Output: prints → Name: Raj | role=engineer
    # Rule: join kwargs as key=value separated by " | "
    print(f"Name: {name} | " + " | ".join([f"{k}={v}" for k, v in kwargs.items()]))

def word_lengths(*args):
    # Input:  word_lengths("hi", "hello", "hey")
    # Output: {"hi": 2, "hello": 5, "hey": 3}
    # Rule: each word maps to its length
    result = {}
    for arg in args:
        result[arg] = len(arg)
    return result

def word_lengths(*args):
    return {word : len(word) for word in args}


# ===== SECTION 3: Slicing =====
# Reminder: lst[start:stop:step]
# lst[1::2]   → every other element starting at index 1
# lst[::-1]   → reversed
# lst[-3:]    → last 3 elements

def every_other(lst):
    # Input:  [10, 20, 30, 40, 50]
    # Output: [20, 40]
    # Rule: elements at index 1, 3, 5... (skip index 0, 2, 4...)
    return [lst[i] for i in range(1,len(lst),2)]
        
def every_other(lst):  
    return lst[1::2]     

def last_three_reversed(lst):
    # Input:  [1, 2, 3, 4, 5]
    # Output: [5, 4, 3]
    # Rule: take last 3, then reverse them
    return lst[:-4:-1]

def is_palindrome(s):
    # Input:  "racecar"
    # Output: True
    # Input:  "hello"
    # Output: False
    # Rule: one line only, use slicing (no loops)
    return s == s[::-1]

# ===== SECTION 4: Dict Building =====
from collections import Counter
def char_count(s):
    # Input:  "hello"
    # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # Rule: count how many times each character appears
    return Counter(s)

def char_count(s):
    result = {}
    for char in s:
        if char not in result:
            result[char] =1
        else:
            result[char]+=1
    return result

def lists_to_dict(keys, values):
    # Input:  ["a","b","c"], [1,2,3]
    # Output: {"a":1, "b":2, "c":3}
    # Rule: pair each key with its matching value (hint: zip)
    return {k:v for k, v in zip(keys,values)}

def invert_dict(d):
    # Input:  {"a": 1, "b": 2}
    # Output: {1: "a", 2: "b"}
    # Rule: swap keys and values
    return {v:k for k, v in d.items()}

# ===== SECTION 5: String Manipulation =====

def title_case(s):
    # Input:  "hELLO wORLD"
    # Output: "Hello World"
    # Rule: first letter uppercase, rest lowercase, for every word
    return s.title()

def remove_spaces(s):
    # Input:  "hello world"
    # Output: "helloworld"
    # Rule: remove ALL spaces (including middle and edges)
    return s.replace(' ','')

def word_count(sentence):
    # Input:  "the cat sat on the mat"
    # Output: {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
    # Rule: count how many times each word appears
    result = sentence.split(' ')
    output = {}
    for word in result:
        if word not in output:
            output[word]= 1
        else:
            output[word]+=1
    return output
def word_count(sentence):
    result = sentence.split(' ')
    return Counter(result)

# ===== TESTS =====
def test(label, got, expected):
    status = "PASS" if got == expected else f"FAIL got {got}, expected {expected}"
    print(f"{label}: {status}")

print("--- Section 1: In-place ---")
nums = [1, -2, 3, -4, 5]; remove_negatives(nums)
test("Q1 remove_negatives", nums, [1, 3, 5])

nums = [1, 2, 2, 3, 3, 4]; remove_dupes(nums)
test("Q2 remove_dupes", nums, [1, 2, 3, 4])

nums = [1, 2, 3, 4, 5]; double_evens(nums)
test("Q3 double_evens", nums, [1, 4, 3, 8, 5])

print("\n--- Section 2: *args / **kwargs ---")
test("Q4 average(1,2,3)", average(1, 2, 3), 2.0)
test("Q4 average(10,20)", average(10, 20), 15.0)
print("Q5 introduce (check manually):")
introduce("Nitu", age=25, city="Pune")
introduce("Raj", role="engineer")
test("Q6 word_lengths", word_lengths("hi", "hello", "hey"), {"hi": 2, "hello": 5, "hey": 3})

print("\n--- Section 3: Slicing ---")
test("Q7 every_other", every_other([10, 20, 30, 40, 50]), [20, 40])
test("Q8 last_three_reversed", last_three_reversed([1, 2, 3, 4, 5]), [5, 4, 3])
test("Q9 palindrome racecar", is_palindrome("racecar"), True)
test("Q9 palindrome hello", is_palindrome("hello"), False)

print("\n--- Section 4: Dict Building ---")
test("Q10 char_count", char_count("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
test("Q11 lists_to_dict", lists_to_dict(["a","b","c"], [1,2,3]), {"a":1,"b":2,"c":3})
test("Q12 invert_dict", invert_dict({"a":1,"b":2}), {1:"a",2:"b"})

print("\n--- Section 5: String ---")
test("Q13 title_case", title_case("hELLO wORLD"), "Hello World")
test("Q14 remove_spaces", remove_spaces("hello world"), "helloworld")
test("Q15 word_count", word_count("the cat sat on the mat"), {'the':2,'cat':1,'sat':1,'on':1,'mat':1})