"""
DAY 2+ — 40 practice questions in 10 patterns (4 per pattern)
Write each function yourself under its question. No hints — just input -> output.
Run:  python python_practice_set2.py        (shows PASS / FAIL / not written yet)
Tip: do one pattern (4 questions) in one sitting; re-do any FAIL two days later.
"""


# ==========================================================================
# PATTERN A — Loop with a running value
# ==========================================================================

# Q1. Count how many numbers in the list are negative.
#     Function: count_negatives(nums)
#     count_negatives([3, -1, -4, 0])  ->  2
#     count_negatives([])  ->  0
#     count_negatives([5, 6])  ->  0
def count_negatives(nums):
    result = 0
    for num in nums:
        if num < 0:
            result+=1
    return result 


# Q2. Return the largest number in a non-empty list WITHOUT using max().
#     Function: max_value(nums)
#     max_value([3, 9, 2])  ->  9
#     max_value([-5, -2, -9])  ->  -2
#     max_value([7])  ->  7
def max_value(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

# Q3. Return a list where each position holds the sum of all numbers up to and including that position.
#     Function: running_sum(nums)
#     running_sum([1, 2, 3, 4])  ->  [1, 3, 6, 10]
#     running_sum([5])  ->  [5]
#     running_sum([])  ->  []
def running_sum(nums):
    result = []
    sum_result = 0
    for num in nums:
        sum_result+=num
        result.append(sum_result)        
    return result

# Q4. Return the second largest DISTINCT value; return None if it doesn't exist.
#     Function: second_largest(nums)
#     second_largest([4, 1, 7, 3])  ->  4
#     second_largest([5, 5, 2])  ->  2
#     second_largest([5, 5])  ->  None
def second_largest(nums):
    unique = sorted(set(nums))
    if len(unique)<2:
        return None
    return unique[-2]

# ==========================================================================
# PATTERN B — Transform / filter a list (comprehensions)
# ==========================================================================

# Q5. Return the length of each word.
#     Function: lengths(words)
#     lengths(['hi', 'hello', ''])  ->  [2, 5, 0]
#     lengths([])  ->  []
def lengths(words):
    return [len(word) for word in words]


# Q6. Return only the words with at least n characters, in order.
#     Function: only_long(words, n)
#     only_long(['a', 'abc', 'abcd'], 3)  ->  ['abc', 'abcd']
#     only_long(['hi'], 5)  ->  []
def only_long(words,n):
    return [word for word in words if len(word)>= n]


# Q7. Convert each Celsius temperature to Fahrenheit (F = C * 9/5 + 32).
#     Function: celsius_to_f(temps)
#     celsius_to_f([0, 100, -40])  ->  [32.0, 212.0, -40.0]
#     celsius_to_f([])  ->  []
def celsius_to_f(temps):
    return [t*9/5+32 for t in temps]

# Q8. Return each name with only its first letter capitalised.
#     Function: capitalize_names(names)
#     capitalize_names(['ravi', 'ANU', 'bala'])  ->  ['Ravi', 'Anu', 'Bala']
#     capitalize_names([])  ->  []
def capitalize_names(names):
    return [name.title() for name in names]


# ==========================================================================
# PATTERN C — Count with a dictionary
# ==========================================================================

# Q9. Return a dict of each character and how many times it appears.
#     Function: char_count(s)
#     char_count('banana')  ->  {'b': 1, 'a': 3, 'n': 2}
#     char_count('')  ->  {}
def char_count(s):
    result = {}
    for char in s:
        if char not in result:
            result[char] = 1
        else:
            result[char]+=1
    return result 

# Q10. Return the word that appears most often; if tied, the alphabetically first one.
#     Function: most_common_word(text)
#     most_common_word('a b a c b a')  ->  'a'
#     most_common_word('x y y x')  ->  'x'
#     most_common_word('gpu')  ->  'gpu'
def most_common_word(text):
    new_text = text.split()
    new_dict = {}
    for t in new_text:
        if t not in new_dict:
            new_dict[t] = 1
        else:
            new_dict[t] +=1
    max_count = max(new_dict.values())
    tied_words = [word for word, count in new_dict.items() if count == max_count ]
    return min(tied_words)



# Q11. Return the first character that appears exactly once; '' if none.
#     Function: first_unique_char(s)
#     first_unique_char('leetcode')  ->  'l'
#     first_unique_char('loveleetcode')  ->  'v'
#     first_unique_char('aabb')  ->  ''
def first_unique_char(s):
    from collections import Counter
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return ''

# Q12. Return True if the two words use exactly the same letters the same number of times.
#     Function: are_anagrams(a, b)
#     are_anagrams('listen', 'silent')  ->  True
#     are_anagrams('rat', 'car')  ->  False
#     are_anagrams('aab', 'abb')  ->  False
def are_anagrams(a,b):
    from collections import Counter
    if Counter(a) == Counter(b):
        return True
    return False

# ==========================================================================
# PATTERN D — Use a set
# ==========================================================================

# Q13. Return the values present in both lists, sorted, without duplicates.
#     Function: common_elements(a, b)
#     common_elements([1, 2, 3, 4, 4], [3, 4, 5])  ->  [3, 4]
#     common_elements([1, 2], [3])  ->  []
def common_elements(a,b):
    return sorted(set(a) & set(b))

# Q14. Remove duplicates but keep the order in which values first appeared.
#     Function: unique_in_order(items)
#     unique_in_order([3, 1, 3, 2, 1])  ->  [3, 1, 2]
#     unique_in_order(['a', 'a'])  ->  ['a']
#     unique_in_order([])  ->  []
def unique_in_order(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

# Q15. Return the numbers from 1 to n that are not in nums, sorted.
#     Function: missing_numbers(nums, n)
#     missing_numbers([1, 2, 4, 6], 6)  ->  [3, 5]
#     missing_numbers([1, 2, 3], 3)  ->  []
def missing_numbers(nums, n):
    missing_number = []
    for num in range(1,n+1):
        if num not in nums:
            missing_number.append(num)
    return missing_number

# Q16. Return True if two numbers at different positions add up to target.
#     Function: two_sum_exists(nums, target)
#     two_sum_exists([2, 7, 11, 15], 9)  ->  True
#     two_sum_exists([1, 2, 3], 7)  ->  False
#     two_sum_exists([3, 3], 6)  ->  True
#     two_sum_exists([3], 6)  ->  False
def two_sum_exists(nums, target):
    seen = set()
    for num in nums:
        if (target - num) in seen:
            return True
        seen.add(num)
    return False


# ==========================================================================
# PATTERN E — Sort with a key
# ==========================================================================

# Q17. Sort words shortest first; same length -> alphabetical.
#     Function: sort_by_length(words)
#     sort_by_length(['banana', 'kiwi', 'apple', 'fig'])  ->  ['fig', 'kiwi', 'apple', 'banana']
#     sort_by_length([])  ->  []
def sort_by_length(words):
    return sorted(words, key = lambda x: (len(x), x))

# Q18. scores is a dict name -> score. Return the k names with the highest scores; ties alphabetical.
#     Function: top_k_scores(scores, k)
#     top_k_scores({'a': 50, 'b': 90, 'c': 70}, 2)  ->  ['b', 'c']
#     top_k_scores({'x': 10, 'y': 10, 'z': 5}, 2)  ->  ['x', 'y']
def top_k_scores(scores, k):
    sorted_score = sorted(scores, key = lambda x: (-scores[x], x))
    return sorted_score[:k]


# Q19. Sort words by their last letter.
#     Function: sort_by_last_char(words)
#     sort_by_last_char(['abc', 'xya', 'mnb'])  ->  ['xya', 'mnb', 'abc']
#     sort_by_last_char(['q'])  ->  ['q']
def sort_by_last_char(words):
    return sorted(words, key = lambda x:(x[-1]))


# Q20. people is a list of (name, age). Return the name of the oldest; if tied, the one listed first.
#     Function: oldest_person(people)
#     oldest_person([('a', 30), ('b', 45), ('c', 45)])  ->  'b'
#     oldest_person([('solo', 20)])  ->  'solo'
def oldest_person(people):
    sorted_people = sorted(people, key = lambda x:(-x[1]) )
    return sorted_people[0][0]

# ==========================================================================
# PATTERN F — Build / transform a dictionary
# ==========================================================================

# Q21. Group words by length: length -> list of words in original order.
#     Function: group_by_length(words)
#     group_by_length(['hi', 'yo', 'cat', 'a'])  ->  {2: ['hi', 'yo'], 3: ['cat'], 1: ['a']}
#     group_by_length([])  ->  {}
def group_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length]= [word]
        else:
            result[length].append(word)      
    return result


# Q22. Group words that are anagrams. Key = the word's letters sorted and joined; value = list of words in original order.
#     Function: group_anagrams(words)
#     group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])  ->  {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
#     group_anagrams([])  ->  {}
def group_anagrams(words):
    result = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in result:
            result[key]= [word]
        else:
            result[key].append(word)
    return result

# Q23. Return a new dict keeping only entries whose value is at least min_value.
#     Function: filter_dict(d, min_value)
#     filter_dict({'a': 5, 'b': 1, 'c': 9}, 5)  ->  {'a': 5, 'c': 9}
#     filter_dict({'a': 1}, 2)  ->  {}
def filter_dict(d, min_value):
    result = {}
    for k, v in d.items():
        if v >= min_value:
            result[k] = v
    return result



# Q24. Return the key that has the largest value (dict is non-empty, no ties).
#     Function: key_with_max_value(d)
#     key_with_max_value({'a': 5, 'b': 9, 'c': 2})  ->  'b'
#     key_with_max_value({'only': -1})  ->  'only'
def key_with_max_value(d):
    new_dict = sorted(d, key = lambda x: -d[x])
    return new_dict[0]

# ==========================================================================
# PATTERN G — Nested lists / 2-D grids
# ==========================================================================

# Q25. Return the sum of every number in a 2-D list.
#     Function: matrix_sum(matrix)
#     matrix_sum([[1, 2], [3, 4]])  ->  10
#     matrix_sum([[]])  ->  0
def matrix_sum(matrix):
    total = 0
    for num in matrix:
        total +=sum(num)
    return total

# Q26. Turn rows into columns.
#     Function: transpose(matrix)
#     transpose([[1, 2, 3], [4, 5, 6]])  ->  [[1, 4], [2, 5], [3, 6]]
#     transpose([[7]])  ->  [[7]]
def transpose(matrix):
    return [list(num) for num in zip(*matrix)]

# Q27. Return a list with the sum of each row.
#     Function: row_sums(matrix)
#     row_sums([[1, 2], [3, 4], [5, 6]])  ->  [3, 7, 11]
#     row_sums([])  ->  []
def row_sums(matrix):
    return [sum(num) for num in matrix]


# Q28. Split a list into consecutive chunks of the given size (last chunk may be smaller).
#     Function: chunk_list(items, size)
#     chunk_list([1, 2, 3, 4, 5], 2)  ->  [[1, 2], [3, 4], [5]]
#     chunk_list([1, 2, 3], 3)  ->  [[1, 2, 3]]
#     chunk_list([], 4)  ->  []
def chunk_list(items, size):
    result = []
    for i in range(0, len(items), size):
        result.append(items[i:i+size])
    return result


# ==========================================================================
# PATTERN H — *args, **kwargs, default arguments
# ==========================================================================

# Q29. Return the product of any number of numbers; 1 if none are given.
#     Function: multiply_all(...)
#     multiply_all(2, 3, 4)  ->  24
#     multiply_all()  ->  1
#     multiply_all(5)  ->  5
def multiply_all(*args):
    result = 1
    for num in args:
        result*=num
    return result

# Q30. Return the longest of any number of words; if tied, the first; '' if none.
#     Function: longest_word(...)
#     longest_word('hi', 'hello', 'hey')  ->  'hello'
#     longest_word('ab', 'cd')  ->  'ab'
#     longest_word()  ->  ''
def longest_word(*args):
    result = ''
    for word in args:
        if len(word)> len(result):
            result = word
    return result

# Q31. Add any named parameters as a query string, in the order given.
#     Function: build_url(base, ...)
#     build_url('api.com/search', q='gpu', page=2)  ->  'api.com/search?q=gpu&page=2'
#     build_url('api.com')  ->  'api.com'
def build_url(base, **kwargs):
    if not kwargs:
        return base
    parts = [f"{k}={v}" for k, v in kwargs.items()]
    return base + "?" + "&".join(parts)

# Q32. Return a greeting; the greeting word is optional and defaults to 'Hello'.
#     Function: greet(name, greeting='Hello')
#     greet('Nitu')  ->  'Hello, Nitu!'
#     greet('Nitu', 'Hi')  ->  'Hi, Nitu!'
#     greet('Ravi', greeting='Welcome')  ->  'Welcome, Ravi!'
def greet(name, greeting = 'Hello'):
    return f"{greeting}, {name}!"

# ==========================================================================
# PATTERN I — Strings
# ==========================================================================

# Q33. Reverse the order of words in a sentence.
#     Function: reverse_words(s)
#     reverse_words('I love python')  ->  'python love I'
#     reverse_words('single')  ->  'single'
def reverse_words(s):
    return ' '.join(s.split()[::-1])
        

# Q34. Return True if the text reads the same backwards, ignoring case, spaces and punctuation.
#     Function: is_palindrome(s)
#     is_palindrome('Race car')  ->  True
#     is_palindrome('hello')  ->  False
#     is_palindrome('A man, a plan, a canal: Panama')  ->  True
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalpha())
    return cleaned == cleaned[::-1]

# Q35. Count the vowels (a, e, i, o, u), upper or lower case.
#     Function: count_vowels(s)
#     count_vowels('Generative AI')  ->  7
#     count_vowels('xyz')  ->  0
def count_vowels(s):
    vowels = ['a','e','i', 'o', 'u']
    total = 0
    for vowel in s.strip().lower():
        if vowel in vowels:
         total +=1
    return total

def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

# Q36. Compress runs of repeated characters as character + count.
#     Function: compress(s)
#     compress('aaabbc')  ->  'a3b2c1'
#     compress('abc')  ->  'a1b1c1'
#     compress('')  ->  ''
def compress(s):
    new_dict = {}
    for c in s:
        if c in new_dict:
            new_dict[c]+=1
        else:
            new_dict[c]=1
    return ''.join(f"{k}{v}" for k, v in new_dict.items())

from collections import Counter
def compress(s):
    return ''.join(f"{c}{n}" for c, n in Counter(s).items())
# ==========================================================================
# PATTERN J — Mixed, real-world
# ==========================================================================

# Q37. transactions is a list of (category, amount). Return total amount per category.
#     Function: total_by_category(transactions)
#     total_by_category([('food', 100), ('travel', 50), ('food', 30)])  ->  {'food': 130, 'travel': 50}
#     total_by_category([])  ->  {}
def total_by_category(transactions):
    result = {}
    for category, amount in transactions:  # unpack here
        if category not in result:
            result[category] = amount
        else:
            result[category] += amount
    return result

# Q38. Swap keys and values; values may repeat, so map each value to a LIST of keys in original order.
#     Function: invert_with_duplicates(d)
#     invert_with_duplicates({'a': 1, 'b': 2, 'c': 1})  ->  {1: ['a', 'c'], 2: ['b']}
#     invert_with_duplicates({})  ->  {}
def invert_with_duplicates(d):
    result = {}
    for k, v in d.items():
        if v not in result:
            result[v] = [k]
        else:
            result[v].append(k)
    return result

def invert_with_duplicates(d):
    result = {}
    for k,v in d.items():
        result.setdefault(v, []).append(k)
    return result

# Q39. Merge any number of count dictionaries by adding values for the same key.
#     Function: merge_many(...)
#     merge_many({'a': 1}, {'a': 2, 'b': 1}, {'b': 5})  ->  {'a': 3, 'b': 6}
#     merge_many()  ->  {}

def merge_many(*args):
    result = {}
    for pair in args:
        for k, v in pair.items():
            if k not in result:
                result[k]= v
            else:
                result[k]+=v
    return result

def merge_many(*args):
    result = {}
    for pair in args:
        for k, v in pair.items():
            result[k] = result.get(k, 0)+v
    return result

# Q40. records is a list of (name, score). Return each student's average score.
#     Function: average_score_per_student(records)
#     average_score_per_student([('ravi', 80), ('anu', 90), ('ravi', 100)])  ->  {'ravi': 90.0, 'anu': 90.0}
#     average_score_per_student([])  ->  {}
def average_score_per_student(records):
    result = {}
    for k, v in records:
        if k not in result:
            result[k] = [v, 1]
        else:
            result[k] = [result[k][0]+v, result[k][1]+1]
    for k, v in result.items():
        result[k] = result[k][0]/result[k][1]
    return result
        

# ---------------------------------------------------------------- self-check (don't edit)
_TESTS = [(1, 'count_negatives', ([3, -1, -4, 0],), {}, 2), (1, 'count_negatives', ([],), {}, 0), (1, 'count_negatives', ([5, 6],), {}, 0), (2, 'max_value', ([3, 9, 2],), {}, 9), (2, 'max_value', ([-5, -2, -9],), {}, -2), (2, 'max_value', ([7],), {}, 7), (3, 'running_sum', ([1, 2, 3, 4],), {}, [1, 3, 6, 10]), (3, 'running_sum', ([5],), {}, [5]), (3, 'running_sum', ([],), {}, []), (4, 'second_largest', ([4, 1, 7, 3],), {}, 4), (4, 'second_largest', ([5, 5, 2],), {}, 2), (4, 'second_largest', ([5, 5],), {}, None), (5, 'lengths', (['hi', 'hello', ''],), {}, [2, 5, 0]), (5, 'lengths', ([],), {}, []), (6, 'only_long', (['a', 'abc', 'abcd'], 3), {}, ['abc', 'abcd']), (6, 'only_long', (['hi'], 5), {}, []), (7, 'celsius_to_f', ([0, 100, -40],), {}, [32.0, 212.0, -40.0]), (7, 'celsius_to_f', ([],), {}, []), (8, 'capitalize_names', (['ravi', 'ANU', 'bala'],), {}, ['Ravi', 'Anu', 'Bala']), (8, 'capitalize_names', ([],), {}, []), (9, 'char_count', ('banana',), {}, {'b': 1, 'a': 3, 'n': 2}), (9, 'char_count', ('',), {}, {}), (10, 'most_common_word', ('a b a c b a',), {}, 'a'), (10, 'most_common_word', ('x y y x',), {}, 'x'), (10, 'most_common_word', ('gpu',), {}, 'gpu'), (11, 'first_unique_char', ('leetcode',), {}, 'l'), (11, 'first_unique_char', ('loveleetcode',), {}, 'v'), (11, 'first_unique_char', ('aabb',), {}, ''), (12, 'are_anagrams', ('listen', 'silent'), {}, True), (12, 'are_anagrams', ('rat', 'car'), {}, False), (12, 'are_anagrams', ('aab', 'abb'), {}, False), (13, 'common_elements', ([1, 2, 3, 4, 4], [3, 4, 5]), {}, [3, 4]), (13, 'common_elements', ([1, 2], [3]), {}, []), (14, 'unique_in_order', ([3, 1, 3, 2, 1],), {}, [3, 1, 2]), (14, 'unique_in_order', (['a', 'a'],), {}, ['a']), (14, 'unique_in_order', ([],), {}, []), (15, 'missing_numbers', ([1, 2, 4, 6], 6), {}, [3, 5]), (15, 'missing_numbers', ([1, 2, 3], 3), {}, []), (16, 'two_sum_exists', ([2, 7, 11, 15], 9), {}, True), (16, 'two_sum_exists', ([1, 2, 3], 7), {}, False), (16, 'two_sum_exists', ([3, 3], 6), {}, True), (16, 'two_sum_exists', ([3], 6), {}, False), (17, 'sort_by_length', (['banana', 'kiwi', 'apple', 'fig'],), {}, ['fig', 'kiwi', 'apple', 'banana']), (17, 'sort_by_length', ([],), {}, []), (18, 'top_k_scores', ({'a': 50, 'b': 90, 'c': 70}, 2), {}, ['b', 'c']), (18, 'top_k_scores', ({'x': 10, 'y': 10, 'z': 5}, 2), {}, ['x', 'y']), (19, 'sort_by_last_char', (['abc', 'xya', 'mnb'],), {}, ['xya', 'mnb', 'abc']), (19, 'sort_by_last_char', (['q'],), {}, ['q']), (20, 'oldest_person', ([('a', 30), ('b', 45), ('c', 45)],), {}, 'b'), (20, 'oldest_person', ([('solo', 20)],), {}, 'solo'), (21, 'group_by_length', (['hi', 'yo', 'cat', 'a'],), {}, {2: ['hi', 'yo'], 3: ['cat'], 1: ['a']}), (21, 'group_by_length', ([],), {}, {}), (22, 'group_anagrams', (['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],), {}, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}), (22, 'group_anagrams', ([],), {}, {}), (23, 'filter_dict', ({'a': 5, 'b': 1, 'c': 9}, 5), {}, {'a': 5, 'c': 9}), (23, 'filter_dict', ({'a': 1}, 2), {}, {}), (24, 'key_with_max_value', ({'a': 5, 'b': 9, 'c': 2},), {}, 'b'), (24, 'key_with_max_value', ({'only': -1},), {}, 'only'), (25, 'matrix_sum', ([[1, 2], [3, 4]],), {}, 10), (25, 'matrix_sum', ([[]],), {}, 0), (26, 'transpose', ([[1, 2, 3], [4, 5, 6]],), {}, [[1, 4], [2, 5], [3, 6]]), (26, 'transpose', ([[7]],), {}, [[7]]), (27, 'row_sums', ([[1, 2], [3, 4], [5, 6]],), {}, [3, 7, 11]), (27, 'row_sums', ([],), {}, []), (28, 'chunk_list', ([1, 2, 3, 4, 5], 2), {}, [[1, 2], [3, 4], [5]]), (28, 'chunk_list', ([1, 2, 3], 3), {}, [[1, 2, 3]]), (28, 'chunk_list', ([], 4), {}, []), (29, 'multiply_all', (2, 3, 4), {}, 24), (29, 'multiply_all', (), {}, 1), (29, 'multiply_all', (5,), {}, 5), (30, 'longest_word', ('hi', 'hello', 'hey'), {}, 'hello'), (30, 'longest_word', ('ab', 'cd'), {}, 'ab'), (30, 'longest_word', (), {}, ''), (31, 'build_url', ('api.com/search',), {'q': 'gpu', 'page': 2}, 'api.com/search?q=gpu&page=2'), (31, 'build_url', ('api.com',), {}, 'api.com'), (32, 'greet', ('Nitu',), {}, 'Hello, Nitu!'), (32, 'greet', ('Nitu', 'Hi'), {}, 'Hi, Nitu!'), (32, 'greet', ('Ravi',), {'greeting': 'Welcome'}, 'Welcome, Ravi!'), (33, 'reverse_words', ('I love python',), {}, 'python love I'), (33, 'reverse_words', ('single',), {}, 'single'), (34, 'is_palindrome', ('Race car',), {}, True), (34, 'is_palindrome', ('hello',), {}, False), (34, 'is_palindrome', ('A man, a plan, a canal: Panama',), {}, True), (35, 'count_vowels', ('Generative AI',), {}, 7), (35, 'count_vowels', ('xyz',), {}, 0), (36, 'compress', ('aaabbc',), {}, 'a3b2c1'), (36, 'compress', ('abc',), {}, 'a1b1c1'), (36, 'compress', ('',), {}, ''), (37, 'total_by_category', ([('food', 100), ('travel', 50), ('food', 30)],), {}, {'food': 130, 'travel': 50}), (37, 'total_by_category', ([],), {}, {}), (38, 'invert_with_duplicates', ({'a': 1, 'b': 2, 'c': 1},), {}, {1: ['a', 'c'], 2: ['b']}), (38, 'invert_with_duplicates', ({},), {}, {}), (39, 'merge_many', ({'a': 1}, {'a': 2, 'b': 1}, {'b': 5}), {}, {'a': 3, 'b': 6}), (39, 'merge_many', (), {}, {}), (40, 'average_score_per_student', ([('ravi', 80), ('anu', 90), ('ravi', 100)],), {}, {'ravi': 90.0, 'anu': 90.0}), (40, 'average_score_per_student', ([],), {}, {})]


def _check():
    import math
    g = globals()
    results = {}
    names = {}
    for qn, fname, args, kwargs, expected in _TESTS:
        names[qn] = fname
        if results.get(qn) is False or results.get(qn) == "missing":
            continue
        if fname not in g:
            results[qn] = "missing"
            continue
        try:
            got = g[fname](*args, **kwargs)
            ok = got == expected or (isinstance(got, float) and isinstance(expected, (int, float)) and math.isclose(got, expected))
            if isinstance(expected, list) and isinstance(got, list) and len(got) == len(expected):
                ok = ok or all(isinstance(a, float) and math.isclose(a, b) for a, b in zip(got, expected))
        except Exception as e:
            ok = False
            print(f"   Q{qn} {fname}{args}: error {type(e).__name__}: {e}")
        if not ok and fname in g:
            try:
                print(f"   Q{qn} {fname}: for input {args} {kwargs or ''} expected {expected!r}, got {g[fname](*args, **kwargs)!r}")
            except Exception:
                pass
        results[qn] = results.get(qn, True) and ok
    passed = 0
    for qn in sorted(names):
        r = results[qn]
        if r == "missing":
            print(f"....  Q{qn} {names[qn]}  (not written yet)")
        else:
            print(("PASS  " if r else "FAIL  ") + f"Q{qn} {names[qn]}")
            passed += bool(r)
    print(f"\n{passed}/{len(names)} passed")


if __name__ == "__main__":
    _check()