"""
LEETCODE NOTEBOOK 1 — Arrays, Two Pointers, Hash Map, Strings, Prefix Sum
==========================================================================
Problems 1–20
Run:  python notebook1_problems_1_to_20.py
All checks at the bottom.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from collections import defaultdict, Counter


# ══════════════════════════════════════════════════════════════════
# ARRAYS BASICS
# ══════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 1. TWO SUM  (LeetCode 1)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Hash map — store what you've seen, look up what you need
# Big O: Time O(n)  |  Space O(n)
#
# WHAT AM I GETTING?
# An unsorted array of integers and a target number.
# Guaranteed exactly one solution exists.
#
# WHAT AM I SUPPOSED TO DO?
# Find two indices i, j such that nums[i] + nums[j] == target.
# Return [i, j].
#
# WHY NOT BRUTE FORCE?
# Two nested loops check every pair → O(n²). Works but slow.
# Hash map: for each num, check if (target - num) already exists → O(n).
#
# THE THINKING:
# You need the INDEX of the complement, not just whether it exists.
# So store num → index in a dict.
# At each step: if (target - num) is already in map → you found the pair.
# If not → store current num and move on.
#
# MEMORY HOOK: "store what I've seen, look for what I need"

def twoSum(nums, target):
    result = {}                          # num → index
    for i, num in enumerate(nums):
        if target - num not in result:   # complement not seen yet
            result[num] = i              # store current number
        else:
            return [result[target-num], i]   # found the pair


# ──────────────────────────────────────────────────────────────────
# 2. CONTAINS DUPLICATE  (LeetCode 217)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Set for O(1) lookup
# Big O: Time O(n)  |  Space O(n)
#
# WHAT AM I GETTING? An array of integers.
# WHAT AM I SUPPOSED TO DO? Return True if any value appears at least twice.
#
# WHY NOT LIST?
# list lookup is O(n) → total O(n²). Set lookup is O(1) → total O(n).
#
# TWO VERSIONS:
#   Version A (one-liner): always processes full array
#   Version B (early exit): returns True the moment first duplicate found
#   → Version B is better for large arrays with early duplicates
#
# MEMORY HOOK: "seen it before? set says yes in O(1)"

def containsDuplicate(nums):             # Version A — concise
    return len(nums) != len(set(nums))

def containsDuplicateB(nums):            # Version B — early exit (better)
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ══════════════════════════════════════════════════════════════════
# TWO POINTERS
# ══════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 3. REVERSE STRING  (LeetCode 344)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Two pointers — opposite ends, swap inward
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING? A list of characters s.
# WHAT AM I SUPPOSED TO DO? Reverse it IN-PLACE. Return nothing (-> None).
#
# WHY NO RETURN?
# The function modifies s directly. Caller already holds the reference.
# Returning s would work but tells the interviewer you don't understand in-place.
#
# THE THINKING:
# i starts at 0 (left), j starts at end (right). Swap. Move both inward.
# Stop when i >= j (they've met or crossed in the middle).
#
# MEMORY HOOK: "two people walk toward each other, swap as they pass"

def reverseString(s):
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    # no return — in place


# ──────────────────────────────────────────────────────────────────
# 4. VALID PALINDROME  (LeetCode 125)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Two pointers with skip logic
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING? A string with spaces, punctuation, mixed case.
# WHAT AM I SUPPOSED TO DO?
# Return True if it reads the same forward and backward,
# considering only alphanumeric characters, ignoring case.
#
# EASY WAY (but O(n) space):
# cleaned = [c.lower() for c in s if c.isalnum()]
# return cleaned == cleaned[::-1]
#
# WHY TWO POINTERS INSTEAD?
# O(1) space — skip non-alphanumeric in-place, compare from both ends.
#
# KEY:
# isalnum() → True for letters AND digits, False for spaces/punctuation
# .lower() → normalize case before comparing
# Inner while loops skip junk. The i < j guard stops them crossing.
#
# MEMORY HOOK: "skip junk, compare real chars from both ends"

def isPalindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():   # skip non-alphanumeric from left
            i += 1
        while i < j and not s[j].isalnum():   # skip non-alphanumeric from right
            j -= 1
        if s[i].lower() != s[j].lower():      # mismatch → not palindrome
            return False
        i += 1
        j -= 1
    return True


# ──────────────────────────────────────────────────────────────────
# 5. TWO SUM II — SORTED ARRAY  (LeetCode 167)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Two pointers on a sorted array
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING? A SORTED array and a target. 1-indexed output required.
# WHAT AM I SUPPOSED TO DO? Find two numbers that add to target. Return [i+1, j+1].
#
# WHY DOES THIS ONLY WORK ON SORTED ARRAYS?
# sum too big  → move right pointer LEFT  (get a smaller number)
# sum too small → move left pointer RIGHT (get a bigger number)
# Sorted = moving left always decreases, moving right always increases.
# On unsorted, you can't know which direction helps.
#
# MEMORY HOOK: "sorted = you know which direction to squeeze"

def twoSum2(numbers, target):
    index1, index2 = 0, len(numbers) - 1
    while index1 < index2:
        curr = numbers[index1] + numbers[index2]
        if curr == target:
            return [index1 + 1, index2 + 1]   # 1-indexed
        elif curr > target:
            index2 -= 1    # too big → smaller right number
        else:
            index1 += 1    # too small → bigger left number


# ──────────────────────────────────────────────────────────────────
# 6. MOVE ZEROES  (LeetCode 283)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Write pointer (slow pointer) — overwrite in place
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING? An array of integers, some are 0.
# WHAT AM I SUPPOSED TO DO?
# Move all zeroes to the end while keeping non-zero order. In-place.
#
# THE THINKING:
# i = write head. Walk through every num.
# If non-zero → write it at nums[i], advance i.
# Zero → skip it, i doesn't move.
# After loop → everything from i to end gets filled with 0.
#
# MEMORY HOOK: "i = write head. only advance it when you actually write something."

def moveZeroes(nums):
    i = 0
    for num in nums:
        if num != 0:
            nums[i] = num
            i += 1          # only advance when a non-zero is written
    while i < len(nums):    # fill the rest with zeros
        nums[i] = 0
        i += 1


# ══════════════════════════════════════════════════════════════════
# SLIDING WINDOW / GREEDY / DYNAMIC PROGRAMMING
# ══════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 7. BEST TIME TO BUY AND SELL STOCK  (LeetCode 121)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Greedy — track running minimum
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING? Array of prices where prices[i] = price on day i.
# WHAT AM I SUPPOSED TO DO? Find max profit from one buy + one sell (buy before sell).
#
# THE THINKING:
# At every price, ask: "Is this cheaper than my best buy day so far?"
# If yes → update min_price (found a better day to have bought).
# Then ask: "Is (today's price - min_price) the best profit so far?"
# If yes → update max_profit.
# IMPORTANT: check min FIRST. You can't sell before you buy.
#
# MEMORY HOOK: "track the floor. profit = current - floor."

def stocks(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        if price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


# ──────────────────────────────────────────────────────────────────
# 8. MAXIMUM SUBARRAY  (LeetCode 53)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Kadane's Algorithm (Dynamic Programming)
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING? Array of integers (can be negative).
# WHAT AM I SUPPOSED TO DO? Find the contiguous subarray with largest sum.
#
# THE THINKING — Kadane's = the fresh start decision:
# At every number ask: "Is my running history helping or hurting?"
# History is negative → drop it, start fresh from this number.
# History is positive → carry it forward.
# current_sum = your running score RIGHT NOW.
# max_sum = best score you EVER had (scoreboard never forgets your peak).
#
# MEMORY HOOK: "fresh start or carry forward. track the peak separately."

def maxSubArray(nums: list[int]) -> int:
    current_sum = nums[0]
    max_sum = nums[0]
    for num in nums[1:]:           # start from index 1, nums[0] already set
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


# ══════════════════════════════════════════════════════════════════
# WRITE POINTER
# ══════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 9. REMOVE DUPLICATES FROM SORTED ARRAY  (LeetCode 26)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Write pointer (in-place array modification)
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING?
# A SORTED array. Sorted is key — duplicates are always neighbors.
# [1,1,2,2,3] not [1,2,1,3,1].
#
# WHAT AM I SUPPOSED TO DO?
# Remove duplicates IN-PLACE. Return k = count of unique elements.
# First k positions of nums hold the unique values. Rest doesn't matter.
#
# WHAT DOES THE QUESTION REALLY MEAN?
# Not actually deleting — OVERWRITING duplicates with the next unique value.
# [1,1,2,2,3] → compact front → [1,2,3,_,_] → return 3
#
# EDGE CASE — empty list?
# LeetCode guarantees at least 1 element. But in interview: mention it.
# If empty: return 0. Shows you think about edge cases.
#
# WHY NOT BRUTE FORCE?
# New array with only uniques → O(n) space. Question says O(1) space, in-place.
#
# THE THINKING:
# k = 1 because nums[0] is always unique (nothing before it). Slot 0 is done.
# Loop from i = 1. Compare nums[i] with nums[i-1].
# If different → new unique → write at nums[k] → advance k.
# k ONLY moves when you write. That's the whole trick.
#
# MEMORY HOOK: "k is the write head. Position 0 is free. Only move k when you write."

def removeDuplicates(nums: list[int]) -> int:
    k = 1                                   # slot 0 is already done
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:            # new unique found
            nums[k] = nums[i]               # write it at the next open slot
            k += 1                          # move write head forward
    return k


# ──────────────────────────────────────────────────────────────────
# 10. REMOVE ELEMENT  (LeetCode 27)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Write pointer (same family as Remove Duplicates)
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING?
# An array nums and a value val. Array is NOT sorted.
#
# WHAT AM I SUPPOSED TO DO?
# Remove every occurrence of val IN-PLACE.
# Return k = count of elements that are NOT val.
# First k elements of nums should hold the non-val values. Order doesn't matter.
#
# WHAT DOES THE QUESTION REALLY MEAN?
# Same as Move Zeroes but instead of moving zeros to the end,
# you're just keeping everything that is NOT val, overwriting the rest.
#
# EDGE CASE?
# What if the whole array is val? k = 0, loop writes nothing. That's fine.
# What if val doesn't appear? k = len(nums), everything stays.
#
# WHY NOT BRUTE FORCE?
# Could filter into a new array → O(n) space. Must be O(1) here.
#
# THE THINKING:
# k = write head starting at 0.
# Walk through every num. If num != val → it's a keeper → write at nums[k], advance k.
# If num == val → skip it. k doesn't move.
# At end, return k.
#
# CONNECTION TO MOVE ZEROES:
# Move Zeroes: keep non-zeros, fill rest with 0.
# Remove Element: keep non-val elements, don't care about the rest.
# Same write-pointer pattern, simpler because you don't need to fill the tail.
#
# MEMORY HOOK: "k = keeper slot. Only advance when you keep something."

def removeElement(nums: list[int], val: int) -> int:
    w = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[w] = nums[i]
            w += 1
    return w


# ══════════════════════════════════════════════════════════════════
# HASH MAP
# ══════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 11. VALID ANAGRAM  (LeetCode 242)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Hash map — frequency count
# Big O: Time O(n)  |  Space O(1) — at most 26 keys (lowercase letters)
#
# WHAT AM I GETTING?
# Two strings s and t (lowercase English letters).
#
# WHAT AM I SUPPOSED TO DO?
# Return True if t is an anagram of s.
# Anagram = same characters, same frequency, any order.
# "anagram" and "nagaram" → True. "rat" and "car" → False.
#
# EDGE CASE?
# If len(s) != len(t) → immediately False. Can't be anagram.
#
# WHY NOT SORTING?
# Sort both strings, compare → O(n log n). Works but hash map is O(n).
#
# THE THINKING (two approaches):
# Approach A — one dict:
#   Count freq of each char in s (increment).
#   Then walk t, decrement each char's count.
#   If any count goes negative → t has more of that char than s → not anagram.
#
# Approach B — two dicts:
#   Build freq dict for s, freq dict for t. Compare them.
#   Simpler to read, same Big O.
#
# MEMORY HOOK: "same letters same count = anagram. count up, count down, check zeros."

def isAnagram(s: str, t: str) -> bool:
    from collections import Counter
    return Counter(s) == Counter(t)

def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        count[char] = count.get(char, 0) - 1
        if count[char] < 0:
            return False
    return True


# ──────────────────────────────────────────────────────────────────
# 12. RANSOM NOTE  (LeetCode 383)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Hash map — frequency count (same as Valid Anagram)
# Big O: Time O(n)  |  Space O(1) — at most 26 keys
#
# WHAT AM I GETTING?
# Two strings: ransomNote and magazine.
#
# WHAT AM I SUPPOSED TO DO?
# Return True if ransomNote can be constructed using letters from magazine.
# Each letter in magazine can only be used once.
# "aa", "aab" → True. "aa", "ab" → False (need 2 a's but only 1).
#
# DIFFERENCE FROM VALID ANAGRAM:
# Anagram: both strings must use EXACTLY the same letters.
# Ransom Note: ransomNote only needs a SUBSET of magazine's letters.
# Magazine must have AT LEAST as many of each letter as ransomNote needs.
#
# THE THINKING:
# Count freq of every char in magazine (your supply).
# Walk through ransomNote. For each char needed:
#   If supply[char] > 0 → use it, decrement supply.
#   If supply[char] == 0 → can't build the note → return False.
# If you get through the whole note → return True.
#
# MEMORY HOOK: "magazine is your supply. ransom note is your demand. can supply meet demand?"

from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
    rn = Counter(ransomNote)
    m = Counter(magazine)
    for k, v in rn.items():
        if m[k] < rn[k]:
            return False
    return True

def canConstruct(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False
    count = {}
    for char in magazine:
        count[char] = count.get(char, 0) + 1
    for char in ransomNote:
        count[char] = count.get(char, 0) - 1
        if count[char] < 0:
            return False
    return True


# ══════════════════════════════════════════════════════════════════
# PREFIX SUM
# ══════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 13. RUNNING SUM OF 1D ARRAY  (LeetCode 1480)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Prefix Sum
# Big O: Time O(n)  |  Space O(n) — or O(1) if you modify in-place
#
# WHAT AM I GETTING?
# An array of integers nums.
#
# WHAT AM I SUPPOSED TO DO?
# Return runningSum where runningSum[i] = sum of nums[0] through nums[i].
# [1,2,3,4] → [1,3,6,10]
#
# WHAT IS PREFIX SUM / RUNNING SUM?
# At each position, you carry forward the total so far.
# It's like a cumulative total — each element = itself + everything before it.
# This is the foundation for many harder problems (range sum queries, subarray sums).
#
# THE THINKING:
# Option A: build a new array. result[0] = nums[0]. result[i] = result[i-1] + nums[i].
# Option B: modify in place. nums[i] += nums[i-1]. O(1) extra space.
#
# MEMORY HOOK: "each element becomes: itself + everything before it."

def runningSum(nums: list[int]) -> list[int]:
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

def runningSum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums


# ──────────────────────────────────────────────────────────────────
# 14. FIND PIVOT INDEX  (LeetCode 724)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Prefix Sum
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING?
# An array of integers nums.
#
# WHAT AM I SUPPOSED TO DO?
# Find the pivot index: the index where sum of everything to the LEFT
# equals sum of everything to the RIGHT.
# The pivot itself is NOT included in either side.
# Return the leftmost such index, or -1 if none exists.
#
# EXAMPLE:
# [1,7,3,6,5,6] → pivot at index 3 (6).
# Left sum = 1+7+3 = 11. Right sum = 5+6 = 11. ✓
#
# EDGE CASE:
# Index 0 can be pivot — left sum = 0 (nothing left of it).
# Index len-1 can be pivot — right sum = 0.
#
# THE THINKING:
# total = sum of whole array.
# Walk through with left_sum = 0.
# At each index i: right_sum = total - left_sum - nums[i]
# If left_sum == right_sum → found pivot → return i.
# After checking: left_sum += nums[i]
# No need to build a prefix array — just track left_sum and compute right_sum on the fly.
#
# MEMORY HOOK: "left_sum + nums[i] + right_sum = total. solve for right_sum. check if left == right."

def pivotIndex(nums: list[int]) -> int:
    total = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1


# ══════════════════════════════════════════════════════════════════
# STRINGS
# ══════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 15. FIRST UNIQUE CHARACTER IN A STRING  (LeetCode 387)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Hash map — frequency count, then scan
# Big O: Time O(n)  |  Space O(1) — at most 26 keys
#
# WHAT AM I GETTING?
# A string s of lowercase English letters.
#
# WHAT AM I SUPPOSED TO DO?
# Find the first character that appears exactly once. Return its index.
# If no unique character exists, return -1.
# "leetcode" → 0 (l appears once, it's first). "aabb" → -1.
#
# THE THINKING — TWO PASSES:
# Pass 1: Count frequency of every character. Store in a dict.
# Pass 2: Walk the string again in order. First character with count == 1 → return its index.
# Why two passes? You need to FINISH counting before you can declare something unique.
# (Can't know 'l' is unique until you've seen the whole string.)
#
# MEMORY HOOK: "count everything first, then find the first with count 1."

from collections import Counter
def firstUniqChar(s: str) -> int:
    result = Counter(s)
    for i in range(len(s)):
        if result[s[i]] == 1:
            return i
    return -1

def firstUniqChar(s: str) -> int:
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    return -1


# ──────────────────────────────────────────────────────────────────
# 16. VALID ANAGRAM  (LeetCode 242 — string version)
# ──────────────────────────────────────────────────────────────────
# Same as problem 11 above. Already solved there. Skip.


# ──────────────────────────────────────────────────────────────────
# 17. LONGEST COMMON PREFIX  (LeetCode 14)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: String scanning
# Big O: Time O(n * m) where n = number of words, m = length of shortest word  |  Space O(1)
#
# WHAT AM I GETTING?
# An array of strings strs.
#
# WHAT AM I SUPPOSED TO DO?
# Find the longest string that is a prefix of ALL strings in the array.
# ["flower","flow","flight"] → "fl". ["dog","racecar","car"] → "".
#
# EDGE CASE?
# Empty array → return "". Single string → return that string.
#
# THE THINKING:
# Take the first word as the reference prefix.
# Compare it with each other word character by character.
# Shrink the prefix whenever a mismatch is found or a word ends.
# Easy approach: start with strs[0] as prefix. For each other word,
# while the word doesn't START WITH the current prefix → chop one char off the end.
# If prefix becomes "" → return "".
#
# MEMORY HOOK: "start with first word as prefix. shrink it until everyone agrees."

def longestCommonPrefix(strs: list[str]) -> str:
    prefix = strs[0]
    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix


# ──────────────────────────────────────────────────────────────────
# 18. FIND THE INDEX OF THE FIRST OCCURRENCE IN A STRING  (LeetCode 28)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: String search / sliding window
# Big O: Time O(n * m) naive  |  Space O(1)
#
# WHAT AM I GETTING?
# haystack: the big string. needle: the substring to find.
#
# WHAT AM I SUPPOSED TO DO?
# Return the index of the first occurrence of needle in haystack.
# Return -1 if needle is not found. "sadbutsad", "sad" → 0. "leetcode", "leeto" → -1.
#
# EASY WAY (Python built-in):
# return haystack.find(needle) — but interviewer may want you to implement it.
#
# THE THINKING (implement it yourself):
# Walk haystack with index i from 0 to len(haystack) - len(needle).
# At each i, check if haystack[i : i+len(needle)] == needle.
# If yes → return i.
# If you exhaust all positions → return -1.
#
# EDGE CASE?
# needle is empty string → return 0 (convention, per LeetCode).
# needle longer than haystack → return -1 immediately.
#
# MEMORY HOOK: "slide a window of needle's size across haystack. check for match."

def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


# ══════════════════════════════════════════════════════════════════
# HASH MAP DEEP
# ══════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 19. MAJORITY ELEMENT  (LeetCode 169)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Hash map frequency OR Boyer-Moore Voting Algorithm
# Big O (hash map): Time O(n)  |  Space O(n)
# Big O (Boyer-Moore): Time O(n)  |  Space O(1)  ← optimal
#
# WHAT AM I GETTING?
# An array nums. Guaranteed: majority element always exists.
# Majority = appears MORE THAN n//2 times.
#
# WHAT AM I SUPPOSED TO DO?
# Return the majority element.
#
# TWO APPROACHES:
#
# Approach A — Hash map:
#   Count frequency of each number.
#   Return the one with count > n//2.
#   Simple. O(n) space.
#
# Approach B — Boyer-Moore Voting (O(1) space, elegant):
#   candidate = None, count = 0
#   Walk array: if count == 0 → new candidate = current num.
#   if current == candidate → count += 1
#   if current != candidate → count -= 1
#   The majority element always survives because it appears > n//2 times.
#   At end, candidate holds the answer.
#
# WHY DOES BOYER-MOORE WORK?
# Think of it as an election. The majority candidate "absorbs" one vote
# whenever it meets itself, loses one vote when it meets an opponent.
# Since it has more than half the votes, it always ends up with votes left.
#
# MEMORY HOOK: "vote up for same, vote down for different. majority always wins."

def majorityElement(nums: list[int]) -> int:
    result = {}
    for num in nums:
        result[num] = result.get(num, 0) + 1
    for k, v in result.items():
        if result[k] > len(nums) // 2:
            return k

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        result = Counter(nums)
        for k, v in result.items():
            if v > len(nums) // 2:
                return k


# ──────────────────────────────────────────────────────────────────
# 20. GROUP ANAGRAMS  (LeetCode 49)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Hash map with tuple key
# Big O: Time O(n * k log k) where k = avg word length  |  Space O(n)
#
# WHAT AM I GETTING?
# An array of strings strs.
#
# WHAT AM I SUPPOSED TO DO?
# Group all anagrams together. Return list of groups.
# ["eat","tea","tan","ate","nat","bat"] → [["eat","tea","ate"],["tan","nat"],["bat"]]
#
# THE THINKING:
# Two strings are anagrams if their SORTED versions are the same.
# "eat" sorted = "aet". "tea" sorted = "aet". Same → same group.
# Use sorted string as the KEY in a dict. Value = list of original words.
# Walk through all words, sort each, add to the matching bucket.
#
# WHY SORTED STRING AS KEY?
# All anagrams of a word produce the same sorted string.
# It's a fingerprint — a canonical form that all anagrams share.
#
# WHY TUPLE NOT LIST?
# dict keys must be hashable. Lists are not hashable. Tuples are.
# tuple(sorted(word)) is your key.
#
# EDGE CASE?
# Single character strings → each is its own group.
#
# MEMORY HOOK: "sort each word → that's its group ID. bucket by group ID."

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = {}
    for word in strs:
        key = tuple(sorted(word))
        if key not in result:
            result[key] = []
        else:
            result[key].append(word)
    return list(result.values())

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = {}
    for word in strs:
        key = tuple(sorted(word))
        result[key] = result.get(key, []) + [word]
    return list(result.values())


# ══════════════════════════════════════════════════════════════════
# CHECKS — ALL AT THE BOTTOM
# Run: python notebook1_problems_1_to_20.py
# ══════════════════════════════════════════════════════════════════

passed = 0
failed = 0
skipped = 0

def check(label, got, expected):
    global passed, failed
    if got == expected:
        print(f"  ✓  {label}")
        passed += 1
    else:
        print(f"  ✗  {label}")
        print(f"       expected : {expected!r}")
        print(f"       you got  : {got!r}")
        failed += 1

def skip(label):
    global skipped
    print(f"  -  {label}  (not solved yet)")
    skipped += 1


print("\n── Q1 : Two Sum ─────────────────────────────")
check("basic",             twoSum([2,7,11,15], 9),       [0,1])
check("not first pair",    twoSum([3,2,4], 6),            [1,2])
check("duplicate values",  twoSum([3,3], 6),              [0,1])

print("\n── Q2 : Contains Duplicate ──────────────────")
check("has duplicate A",   containsDuplicate([1,2,3,1]),  True)
check("no duplicate A",    containsDuplicate([1,2,3,4]),  False)
check("has duplicate B",   containsDuplicateB([1,2,3,1]), True)
check("no duplicate B",    containsDuplicateB([1,2,3,4]), False)

print("\n── Q3 : Reverse String ──────────────────────")
s = ['h','e','l','l','o']; reverseString(s)
check("reversed",          s,                             ['o','l','l','e','h'])

print("\n── Q4 : Valid Palindrome ────────────────────")
check("with punctuation",  isPalindrome("A man, a plan, a canal: Panama"), True)
check("not palindrome",    isPalindrome("race a car"),    False)
check("spaces only",       isPalindrome(" "),             True)

print("\n── Q5 : Two Sum II ──────────────────────────")
check("basic",             twoSum2([2,7,11,15], 9),       [1,2])
check("middle pair",       twoSum2([1,2,3,4,5], 5),       [1,4])

print("\n── Q6 : Move Zeroes ─────────────────────────")
n = [0,1,0,3,12]; moveZeroes(n)
check("basic",             n,                             [1,3,12,0,0])
n2 = [0]; moveZeroes(n2)
check("single zero",       n2,                            [0])

print("\n── Q7 : Best Time Buy/Sell ──────────────────")
check("basic profit",      stocks([7,1,5,3,6,4]),         5)
check("no profit",         stocks([7,6,4,3,1]),            0)

print("\n── Q8 : Maximum Subarray ────────────────────")
check("basic",             maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
check("all negative",      maxSubArray([-1,-2,-3]),        -1)
check("single element",    maxSubArray([5]),                5)

print("\n── Q9 : Remove Duplicates ───────────────────")
a = [0,0,1,1,1,2,2,3,3,4]
check("basic",             removeDuplicates(a),            5)
a2 = [1,1,2]
check("simple",            removeDuplicates(a2),           2)

print("\n── Q10 : Remove Element ─────────────────────")
try:
    r = removeElement([3,2,2,3], 3)
    check("remove 3",      r,                              2)
    r2 = removeElement([0,1,2,2,3,0,4,2], 2)
    check("remove 2",      r2,                             5)
except: skip("not solved yet")

print("\n── Q11 : Valid Anagram ──────────────────────")
try:
    check("anagram",       isAnagram("anagram","nagaram"), True)
    check("not anagram",   isAnagram("rat","car"),         False)
except: skip("not solved yet")

print("\n── Q12 : Ransom Note ────────────────────────")
try:
    check("can build",     canConstruct("aa","aab"),       True)
    check("cannot build",  canConstruct("aa","ab"),        False)
except: skip("not solved yet")

print("\n── Q13 : Running Sum ────────────────────────")
try:
    check("basic",         runningSum([1,2,3,4]),          [1,3,6,10])
    check("single",        runningSum([5]),                 [5])
except: skip("not solved yet")

print("\n── Q14 : Pivot Index ────────────────────────")
try:
    check("pivot at 3",    pivotIndex([1,7,3,6,5,6]),      3)
    check("no pivot",      pivotIndex([1,2,3]),            -1)
    check("pivot at 0",    pivotIndex([2,1,-1]),            0)
except: skip("not solved yet")

print("\n── Q15 : First Unique Char ──────────────────")
try:
    check("leetcode",      firstUniqChar("leetcode"),      0)
    check("loveleetcode",  firstUniqChar("loveleetcode"),  2)
    check("aabb",          firstUniqChar("aabb"),         -1)
except: skip("not solved yet")

print("\n── Q17 : Longest Common Prefix ──────────────")
try:
    check("fl",            longestCommonPrefix(["flower","flow","flight"]), "fl")
    check("no prefix",     longestCommonPrefix(["dog","racecar","car"]),    "")
except: skip("not solved yet")

print("\n── Q18 : Find Needle in Haystack ────────────")
try:
    check("found at 0",    strStr("sadbutsad","sad"),       0)
    check("not found",     strStr("leetcode","leeto"),     -1)
    check("found at 4",    strStr("sadbutsad","but"),       3)
except: skip("not solved yet")

print("\n── Q19 : Majority Element ───────────────────")
try:
    check("basic",         majorityElement([3,2,3]),        3)
    check("all same",      majorityElement([2,2,1,1,1,2,2]),2)
except: skip("not solved yet")

print("\n── Q20 : Group Anagrams ─────────────────────")
try:
    result = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    result_sorted = sorted([sorted(g) for g in result])
    expected_sorted = sorted([sorted(g) for g in [["bat"],["nat","tan"],["ate","eat","tea"]]])
    check("groups correct", result_sorted,                  expected_sorted)
except: skip("not solved yet")

total = passed + failed
print(f"\n{'='*52}")
print(f"  SOLVED : {passed} passed / {total} attempted  |  {skipped} not yet written")
if failed == 0 and passed > 0:
    print("  All solved problems passing. Keep going.")
elif failed > 0:
    print(f"  Fix the {failed} failing test(s).")
print('='*52)