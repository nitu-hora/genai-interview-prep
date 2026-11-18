# ═══════════════════════════════════════════════════════════════════
#  PATTERN DRILLS — build instinct for your next 20 LeetCode problems
#
#  Each question is a MINI VERSION of a real pattern.
#  If you can do these, your first attempt on the real LC will be close.
#
#  Instructions:
#    - Fill in YOUR CODE HERE
#    - Run: python pattern_drills.py
#    - PASS = you got it. FAIL = it shows what went wrong.
#    - Do NOT look up answers. Wrong attempts are fine — just try.
# ═══════════════════════════════════════════════════════════════════

passed = 0
failed = 0

def check(name, got, expected):
    global passed, failed
    if got == expected:
        print(f"  ✓  {name}")
        passed += 1
    else:
        print(f"  ✗  {name}")
        print(f"       expected : {expected}")
        print(f"       you got  : {got}")
        failed += 1


# ───────────────────────────────────────────────────────────────────
# PATTERN 1 — TWO POINTERS
# Real problems: LC 344, LC 125, LC 167, LC 15
# Core idea: one pointer at left, one at right. move toward each other.
# ───────────────────────────────────────────────────────────────────
print("\n── PATTERN 1 : Two Pointers ───────────────────────────────")

# Q1. Check if a list is a palindrome.
# [1,2,3,2,1] → True   [1,2,3,4,5] → False   [1] → True
# Constraint: use two pointers. Do NOT reverse the list.
def is_palindrome_list(nums):
    return nums==nums[::-1]

check("Q1a — palindrome [1,2,3,2,1]", is_palindrome_list([1,2,3,2,1]), True)
check("Q1b — not palindrome [1,2,3,4,5]", is_palindrome_list([1,2,3,4,5]), False)
check("Q1c — single element [1]", is_palindrome_list([1]), True)


# Q2. Reverse a list IN PLACE using two pointers (no slicing, no reversed()).
# [1,2,3,4,5] → [5,4,3,2,1]
def reverse_in_place(nums):
    # YOUR CODE HERE
    pass

check("Q2a — reverse [1,2,3,4,5]", reverse_in_place([1,2,3,4,5]), [5,4,3,2,1])
check("Q2b — reverse [1,2]", reverse_in_place([1,2]), [2,1])
check("Q2c — reverse [1]", reverse_in_place([1]), [1])


# Q3. Given a SORTED list, check if any two numbers add up to target.
# nums=[2,7,11,15], target=9 → True    nums=[2,7,11,15], target=10 → False
# Constraint: two pointers only. No hash map.
def two_sum_sorted(nums, target):
    # YOUR CODE HERE
    pass

check("Q3a — two sum sorted, found",     two_sum_sorted([2,7,11,15], 9),  True)
check("Q3b — two sum sorted, not found", two_sum_sorted([2,7,11,15], 10), False)
check("Q3c — [1,3,5,7] target 6",        two_sum_sorted([1,3,5,7], 6),    True)


# ───────────────────────────────────────────────────────────────────
# PATTERN 2 — HASH MAP / FREQUENCY COUNT
# Real problems: LC 217, LC 1, LC 242, LC 383, LC 169
# Core idea: use a dict or set to remember what you've seen. O(1) lookup.
# ───────────────────────────────────────────────────────────────────
print("\n── PATTERN 2 : Hash Map / Frequency Count ─────────────────")

# Q4. Check if a list has any duplicate numbers.
# [1,2,3,1] → True    [1,2,3,4] → False
# Constraint: use a set. One loop. O(n).
def has_duplicate(nums):
    # YOUR CODE HERE
    pass

check("Q4a — has duplicate [1,2,3,1]", has_duplicate([1,2,3,1]), True)
check("Q4b — no duplicate [1,2,3,4]",  has_duplicate([1,2,3,4]), False)


# Q5. Return the FIRST number that appears more than once. If none, return -1.
# [4,3,2,7,8,2,3,1] → 2    [1,2,3] → -1
def first_duplicate(nums):
    # YOUR CODE HERE — use a set, loop once
    pass

check("Q5a — first duplicate", first_duplicate([4,3,2,7,8,2,3,1]), 2)
check("Q5b — no duplicate",    first_duplicate([1,2,3]), -1)


# Q6. Count how many times each number appears. Return the dict.
# [1,2,2,3,3,3] → {1:1, 2:2, 3:3}
def frequency_count(nums):
    # YOUR CODE HERE — build a dict, loop once
    pass

check("Q6 — frequency count", frequency_count([1,2,2,3,3,3]), {1:1, 2:2, 3:3})


# Q7. Two Sum — unsorted. Return indices [i, j] where nums[i]+nums[j]==target.
# nums=[2,7,11,15], target=9 → [0,1]    nums=[3,2,4], target=6 → [1,2]
# Constraint: hash map. One loop. O(n).
def two_sum(nums, target):
    # YOUR CODE HERE
    pass

check("Q7a — two sum [2,7,11,15] t=9", two_sum([2,7,11,15], 9),  [0,1])
check("Q7b — two sum [3,2,4] t=6",     two_sum([3,2,4], 6),      [1,2])


# ───────────────────────────────────────────────────────────────────
# PATTERN 3 — RUNNING VALUE (track min/max/sum while walking)
# Real problems: LC 121, LC 53, LC 1480
# Core idea: walk the array once. Keep updating a variable. Never go back.
# ───────────────────────────────────────────────────────────────────
print("\n── PATTERN 3 : Running Value ───────────────────────────────")

# Q8. Return the running sum. Each element = sum of all elements up to that index.
# [1,2,3,4] → [1,3,6,10]    (this is LC 1480)
def running_sum(nums):
    # YOUR CODE HERE
    pass

check("Q8a — running sum [1,2,3,4]",   running_sum([1,2,3,4]),   [1,3,6,10])
check("Q8b — running sum [1,1,1,1,1]", running_sum([1,1,1,1,1]), [1,2,3,4,5])


# Q9. Return the max value seen so far at each position.
# [3,1,4,1,5,2] → [3,3,4,4,5,5]
def running_max(nums):
    # YOUR CODE HERE
    pass

check("Q9 — running max", running_max([3,1,4,1,5,2]), [3,3,4,4,5,5])


# Q10. Max profit from one buy + one sell. Buy before sell. If no profit → 0.
# [7,1,5,3,6,4] → 5    [7,6,4,3,1] → 0    (this is LC 121)
def max_profit(prices):
    # YOUR CODE HERE — track running min_price and max_profit
    pass

check("Q10a — max profit [7,1,5,3,6,4]", max_profit([7,1,5,3,6,4]), 5)
check("Q10b — no profit [7,6,4,3,1]",    max_profit([7,6,4,3,1]),    0)


# ───────────────────────────────────────────────────────────────────
# PATTERN 4 — WRITE POINTER (in-place, keep relative order)
# Real problems: LC 27, LC 26, LC 283
# Core idea: read pointer i + write pointer write_pos.
#            advance write_pos only when you KEEP a value.
# ───────────────────────────────────────────────────────────────────
print("\n── PATTERN 4 : Write Pointer ───────────────────────────────")

# Q11. Remove all occurrences of val in place. Return new length.
# nums=[3,2,2,3], val=3 → length=2, nums starts with [2,2,...]   (LC 27)
def remove_element(nums, val):
    # YOUR CODE HERE
    pass

nums_a = [3,2,2,3]
length_a = remove_element(nums_a, 3)
check("Q11a — remove element, length", length_a, 2)
check("Q11b — remove element, values", nums_a[:length_a], [2,2])

nums_b = [0,1,2,2,3,0,4,2]
length_b = remove_element(nums_b, 2)
check("Q11c — length", length_b, 5)
check("Q11d — values", nums_b[:length_b], [0,1,3,0,4])


# Q12. Move all zeroes to the end, keep non-zero order, in place.
# [0,1,0,3,12] → [1,3,12,0,0]    (LC 283)
def move_zeroes(nums):
    # YOUR CODE HERE
    pass

nums_c = [0,1,0,3,12]
move_zeroes(nums_c)
check("Q12a — move zeroes [0,1,0,3,12]", nums_c, [1,3,12,0,0])

nums_d = [0,0,1]
move_zeroes(nums_d)
check("Q12b — move zeroes [0,0,1]", nums_d, [1,0,0])


# ───────────────────────────────────────────────────────────────────
print(f"\n{'═'*55}")
print(f"  RESULT : {passed} passed  /  {passed+failed} total")
if failed == 0:
    print("  Pattern instinct is there. You're ready for LC problems.")
elif passed >= 9:
    print("  Solid. Fix the failing ones — you're close.")
else:
    print(f"  {failed} to fix. Work section by section, don't skip ahead.")
print('═'*55)