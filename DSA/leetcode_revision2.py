"""
LEETCODE NOTEBOOK 2 — Arrays Medium, Linked List, Stack
========================================================
Problems 21–35
Run:  python notebook2_problems_21_to_35.py
All checks at the bottom.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from collections import defaultdict


# ══════════════════════════════════════════════════════════════════
# ARRAYS MEDIUM
# ══════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 21. PRODUCT OF ARRAY EXCEPT SELF  (LeetCode 238)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Prefix product + suffix product
# Big O: Time O(n)  |  Space O(1) extra (output array doesn't count)
#
# WHAT AM I GETTING?
# An array nums. Guaranteed no division needed (the trick isn't division).
#
# WHAT AM I SUPPOSED TO DO?
# Return output array where output[i] = product of ALL elements EXCEPT nums[i].
# [1,2,3,4] → [24,12,8,6]
# (output[0] = 2*3*4=24, output[1] = 1*3*4=12, etc.)
#
# WHY CAN'T YOU JUST DO total_product / nums[i]?
# The problem says you cannot use division. Also: what if nums[i] = 0?
#
# THE THINKING — PREFIX PRODUCT + SUFFIX PRODUCT:
# output[i] = (product of everything to the LEFT of i) * (product of everything to the RIGHT of i)
#
# Pass 1 (left to right): fill output[i] with product of all elements BEFORE i.
# Pass 2 (right to left): multiply output[i] by product of all elements AFTER i.
# Use a running variable for the suffix, no extra array needed.
#
# SUFFIX LOOP DIRECTION: must go RIGHT TO LEFT → range(n-1, -1, -1)
# Going left to right in the suffix pass is the most common bug.
#
# MEMORY HOOK: "left pass fills prefix. right pass multiplies in suffix. result is their product."

def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    sufix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= sufix
        sufix *= nums[i]

    return answer


# ──────────────────────────────────────────────────────────────────
# 22. VALID SUDOKU  (LeetCode 36)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Hash map / Set — validate constraints
# Big O: Time O(1) — board is always 9x9 = 81 cells  |  Space O(1)
#
# WHAT AM I GETTING?
# A 9x9 board with digits '1'-'9' and '.' for empty cells.
#
# WHAT AM I SUPPOSED TO DO?
# Determine if the board is VALID (not necessarily solvable).
# Valid = no duplicate 1-9 in any row, any column, any 3x3 box.
#
# THE THINKING:
# Three sets of constraints to check:
# 1. Each ROW: no digit appears twice.
# 2. Each COLUMN: no digit appears twice.
# 3. Each 3x3 BOX: no digit appears twice.
#
# Use a set per row (9 sets), a set per column (9 sets), a set per box (9 sets).
# Walk every cell. If it's '.', skip.
# If the digit is already in that row's set OR that column's set OR that box's set → invalid.
# Otherwise add it to all three sets.
#
# BOX INDEX TRICK: box_index = (row // 3) * 3 + (col // 3)
# This maps (row, col) → one of 9 box indices (0-8).
#
# MEMORY HOOK: "three rules: row, col, box. use sets. seen twice = invalid."

def isValidSudoku(board: list[list[str]]) -> bool:
    pass  # ← YOUR CODE HERE


# ──────────────────────────────────────────────────────────────────
# 23. ROTATE IMAGE  (LeetCode 48)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Matrix manipulation — transpose + reverse
# Big O: Time O(n²)  |  Space O(1) — in-place
#
# WHAT AM I GETTING?
# An n×n matrix (2D list).
#
# WHAT AM I SUPPOSED TO DO?
# Rotate the image 90 degrees CLOCKWISE, IN-PLACE.
#
# THE TRICK — TWO STEPS:
# Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i]).
#         Rows become columns.
# Step 2: Reverse each row.
# Together these produce a 90° clockwise rotation.
#
# WHY DOES THIS WORK?
# A 90° clockwise rotation sends (row, col) → (col, n-1-row).
# Transpose sends (i,j) → (j,i). Then reversing each row sends (j,i) → (j, n-1-i).
# Combined: (i,j) → (j, n-1-i) = clockwise rotation formula. ✓
#
# MEMORY HOOK: "clockwise = transpose then reverse each row."

def rotate(matrix: list[list[int]]) -> None:
    pass  # ← YOUR CODE HERE


# ──────────────────────────────────────────────────────────────────
# 24. SPIRAL MATRIX  (LeetCode 54)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Matrix traversal with shrinking boundaries
# Big O: Time O(m*n)  |  Space O(1) extra (output list doesn't count)
#
# WHAT AM I GETTING?
# An m×n matrix.
#
# WHAT AM I SUPPOSED TO DO?
# Return all elements in spiral order (→ ↓ ← ↑ then inward repeat).
#
# THE THINKING — SHRINKING BOUNDARIES:
# Track four walls: top, bottom, left, right.
# Go right across top row → shrink top down.
# Go down right column → shrink right left.
# Go left across bottom row → shrink bottom up.
# Go up left column → shrink left right.
# Repeat until boundaries cross.
#
# EDGE CASE?
# Single row: only go right, no going down/left/up needed.
# Single column: only go down. Guard: check top <= bottom and left <= right before each direction.
#
# MEMORY HOOK: "four walls. walk the edge, shrink the wall. repeat inward."

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    pass  # ← YOUR CODE HERE


# ══════════════════════════════════════════════════════════════════
# LINKED LIST
# ══════════════════════════════════════════════════════════════════

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(values):
    """Helper: build a linked list from a Python list."""
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def list_to_array(head):
    """Helper: flatten a linked list back to a Python list for checking."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ──────────────────────────────────────────────────────────────────
# 25. REVERSE LINKED LIST  (LeetCode 206)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Linked list — iterative pointer reversal
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING?
# Head of a singly linked list. 1 → 2 → 3 → 4 → 5 → None
#
# WHAT AM I SUPPOSED TO DO?
# Reverse it in-place. Return the new head.
# 1 → 2 → 3 → 4 → 5 → None  becomes  5 → 4 → 3 → 2 → 1 → None
#
# WHAT DOES THE QUESTION REALLY MEAN?
# Each node has a .next pointer. You need to flip ALL those arrows.
# The last node becomes the new head. The old head becomes the new tail.
#
# EDGE CASE?
# Empty list (head is None) → return None.
# Single node → return it as-is.
#
# WHY NOT BRUTE FORCE?
# Could collect all values, reverse the list, rebuild → O(n) space.
# Must do O(1) space → flip pointers in place.
#
# THE THINKING — THREE-POINTER TECHNIQUE:
# prev = None  (what the current node should now point to)
# curr = head  (the node you're currently reversing)
# nxt  = None  (save next before you overwrite curr.next)
#
# Each step:
#   Save curr.next in nxt (so you don't lose the rest of the list)
#   Flip: curr.next = prev
#   Advance: prev = curr, curr = nxt
# When curr is None, prev is the new head.
#
# WALK THROUGH: 1→2→3→None
#   Step 1: nxt=2, 1.next=None, prev=1, curr=2
#   Step 2: nxt=3, 2.next=1,   prev=2, curr=3
#   Step 3: nxt=None, 3.next=2, prev=3, curr=None
#   Return prev (3) → 3→2→1→None ✓
#
# MEMORY HOOK: "save next. flip pointer. slide forward. when done, prev is the new head."

def reverseList(head: ListNode) -> ListNode:
    pass  # ← YOUR CODE HERE


# ──────────────────────────────────────────────────────────────────
# 26. MERGE TWO SORTED LISTS  (LeetCode 21)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Linked list — merge with dummy head
# Big O: Time O(n + m)  |  Space O(1)
#
# WHAT AM I GETTING?
# Heads of two sorted linked lists: list1 and list2.
# 1→2→4 and 1→3→4
#
# WHAT AM I SUPPOSED TO DO?
# Merge them into one sorted linked list. Return its head.
# Result: 1→1→2→3→4→4
#
# WHAT DOES THE QUESTION REALLY MEAN?
# Don't create new nodes — rearrange the .next pointers of existing nodes.
#
# EDGE CASE?
# One or both lists are empty → return the other one.
#
# THE THINKING — DUMMY HEAD TRICK:
# Create a dummy node (value 0) as the starting point.
# dummy.next will be the actual head of the merged list.
# curr = dummy, your "builder" pointer.
# Compare list1.val and list2.val at each step.
# Attach the smaller one to curr.next. Advance that pointer AND curr.
# When one list runs out, attach the rest of the other list directly.
#
# WHY DUMMY NODE?
# Without it, you need special handling for the very first node.
# With dummy: every node is treated the same way. Cleaner code.
#
# MEMORY HOOK: "dummy head avoids edge cases. compare and pick the smaller. attach the leftovers."

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    pass  # ← YOUR CODE HERE


# ──────────────────────────────────────────────────────────────────
# 27. LINKED LIST CYCLE  (LeetCode 141)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Linked list — Floyd's Cycle Detection (fast/slow pointers)
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING?
# Head of a linked list. May or may not have a cycle (loop).
# A cycle means some node's .next points back to a previous node.
#
# WHAT AM I SUPPOSED TO DO?
# Return True if there is a cycle, False otherwise.
#
# BRUTE FORCE — set of visited nodes:
# Keep a set of node ids. If you see one twice → cycle. O(n) space.
#
# OPTIMAL — Floyd's Cycle Detection (tortoise and hare):
# slow pointer moves 1 step. fast pointer moves 2 steps.
# If there's a cycle, fast will eventually catch up to slow inside the cycle.
# If there's no cycle, fast hits None and you're done.
#
# WHY DOES FAST CATCH SLOW?
# Each iteration, fast gains 1 step on slow inside the cycle.
# So the gap between them shrinks by 1 each time → they must meet.
#
# EDGE CASE?
# Empty list or single node with no cycle → return False immediately.
#
# MEMORY HOOK: "tortoise and hare. if they meet, there's a loop."

def hasCycle(head: ListNode) -> bool:
    pass  # ← YOUR CODE HERE


# ──────────────────────────────────────────────────────────────────
# 28. REMOVE DUPLICATES FROM SORTED LINKED LIST  (LeetCode 83)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Linked list — skip duplicate nodes
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING?
# Head of a SORTED linked list. 1→1→2→3→3
#
# WHAT AM I SUPPOSED TO DO?
# Delete all duplicates so each element appears only once.
# 1→1→2→3→3 → 1→2→3
#
# WHY SORTED MATTERS?
# Because duplicates are always adjacent in a sorted list.
# You only need to check curr.val == curr.next.val.
# If they match, skip curr.next. If not, advance curr.
#
# THE THINKING:
# curr = head.
# While curr and curr.next exist:
#   If curr.val == curr.next.val → curr.next = curr.next.next (skip the duplicate)
#   Else → curr = curr.next (move forward)
# Why not always advance? Because after skipping one duplicate,
# the next node might ALSO be a duplicate of curr.
#
# MEMORY HOOK: "sorted = duplicates are neighbors. skip the next node when values match."

def deleteDuplicates(head: ListNode) -> ListNode:
    pass  # ← YOUR CODE HERE


# ──────────────────────────────────────────────────────────────────
# 29. REMOVE NTH NODE FROM END OF LIST  (LeetCode 19)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Linked list — two pointers with a gap
# Big O: Time O(n)  |  Space O(1)
#
# WHAT AM I GETTING?
# Head of a linked list and an integer n.
# 1→2→3→4→5, n=2
#
# WHAT AM I SUPPOSED TO DO?
# Remove the nth node from the END of the list. Return new head.
# Remove 4 (2nd from end) → 1→2→3→5
#
# BRUTE FORCE:
# Count length L. Remove node at position (L - n). O(n) but two passes.
#
# OPTIMAL — ONE PASS with two pointers:
# Create a dummy node before head.
# fast pointer advances n+1 steps from dummy.
# Then move both fast and slow together until fast hits None.
# Now slow is pointing to the node BEFORE the one to delete.
# slow.next = slow.next.next → done.
#
# WHY n+1 STEPS?
# You want slow to stop one node BEFORE the target (so you can skip it).
# Moving fast n+1 ahead means when fast=None, slow is n+1 steps behind = one before the target.
#
# EDGE CASE?
# Removing the head node (n == length of list) → dummy handles this gracefully.
#
# MEMORY HOOK: "gap of n+1. when fast hits None, slow is just before the target."

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    pass  # ← YOUR CODE HERE


# ──────────────────────────────────────────────────────────────────
# 30. INTERSECTION OF TWO LINKED LISTS  (LeetCode 160)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Linked list — two pointer length equalization
# Big O: Time O(n + m)  |  Space O(1)
#
# WHAT AM I GETTING?
# Heads of two linked lists. They may share a common tail (same node object, not just value).
#
# WHAT AM I SUPPOSED TO DO?
# Return the node where they intersect. Return None if no intersection.
#
# BRUTE FORCE:
# Put all nodes of list A in a set. Walk list B, first match is intersection. O(n) space.
#
# OPTIMAL — TWO POINTER TRICK:
# pA starts at headA, pB starts at headB.
# Each step: advance both.
# When pA reaches end of A, redirect it to headB.
# When pB reaches end of B, redirect it to headA.
# They will meet at the intersection (or both hit None if no intersection).
#
# WHY DOES THIS WORK?
# Both pointers walk the same total distance: len(A) + len(B).
# After the redirect, they're both the same distance from the intersection.
# So they must meet there.
#
# MEMORY HOOK: "swap starting points when you hit the end. same total distance = same arrival."

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    pass  # ← YOUR CODE HERE


# ══════════════════════════════════════════════════════════════════
# STACK
# ══════════════════════════════════════════════════════════════════

# ──────────────────────────────────────────────────────────────────
# 31. VALID PARENTHESES  (LeetCode 20)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Stack — match opening with closing
# Big O: Time O(n)  |  Space O(n)
#
# WHAT AM I GETTING?
# A string containing only '(', ')', '{', '}', '[', ']'.
#
# WHAT AM I SUPPOSED TO DO?
# Return True if the string is valid.
# Valid = every opening bracket has a matching closing bracket in the right order.
# "()" → True. "()[]{}" → True. "(]" → False. "([)]" → False. "{[]}" → True.
#
# EDGE CASE?
# Empty string → True (vacuously valid).
# Odd length → immediately False (can't all be matched).
# Stack is not empty at the end → unmatched opening brackets → False.
#
# THE THINKING:
# Use a stack. Walk through the string.
# If you see an opening bracket → push it onto the stack.
# If you see a closing bracket:
#   Stack must not be empty AND top of stack must be the matching opener.
#   If either fails → return False.
#   If match → pop the opener.
# At the end, stack should be empty.
#
# MATCHING MAP: use a dict: ')':'(', '}':'{', ']':'['
# So when you see ')', look up its expected opener '(' and check the stack top.
#
# MEMORY HOOK: "opening → push. closing → pop and match. empty stack at end = valid."

def isValid(s: str) -> bool:
    pass  # ← YOUR CODE HERE


# ──────────────────────────────────────────────────────────────────
# 32. MIN STACK  (LeetCode 155)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Stack — design with O(1) minimum tracking
# Big O: push/pop/top/getMin all O(1)  |  Space O(n)
#
# WHAT AM I GETTING?
# Nothing — you're designing a class from scratch.
#
# WHAT AM I SUPPOSED TO DO?
# Implement a MinStack with push, pop, top, and getMin.
# getMin() must return the minimum element in O(1) time.
#
# THE TRICK — TWO STACKS:
# Stack 1 (main): stores all values as usual.
# Stack 2 (min_stack): stores the current minimum at each level.
# On push: push value to main, push min(value, min_stack.top) to min_stack.
# On pop: pop from both stacks simultaneously.
# getMin(): just look at min_stack[-1].
#
# WHY TWO STACKS?
# The minimum can change as you push/pop. You need to REMEMBER what the
# minimum was at every level of the stack, so when you pop, you restore
# the previous minimum correctly.
#
# EXAMPLE:
# push(5): main=[5], min_stack=[5]
# push(3): main=[5,3], min_stack=[5,3]
# push(7): main=[5,3,7], min_stack=[5,3,3]  ← min stays 3
# getMin() → 3
# pop():    main=[5,3], min_stack=[5,3]     ← 7 gone, min still 3
# getMin() → 3
# pop():    main=[5], min_stack=[5]         ← 3 gone, min is now 5
# getMin() → 5
#
# MEMORY HOOK: "shadow stack tracks min at every level. pop both together."

class MinStack:
    def __init__(self):
        pass  # ← YOUR CODE HERE

    def push(self, val: int) -> None:
        pass  # ← YOUR CODE HERE

    def pop(self) -> None:
        pass  # ← YOUR CODE HERE

    def top(self) -> int:
        pass  # ← YOUR CODE HERE

    def getMin(self) -> int:
        pass  # ← YOUR CODE HERE


# ──────────────────────────────────────────────────────────────────
# 33. DAILY TEMPERATURES  (LeetCode 739)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Stack — monotonic decreasing stack
# Big O: Time O(n)  |  Space O(n)
#
# WHAT AM I GETTING?
# Array of daily temperatures. temperatures = [73,74,75,71,69,72,76,73]
#
# WHAT AM I SUPPOSED TO DO?
# Return answer array where answer[i] = number of days until a warmer temperature.
# If there's no future warmer day, answer[i] = 0.
# [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]
#
# BRUTE FORCE:
# For each day, scan forward until you find a warmer day → O(n²).
#
# THE THINKING — MONOTONIC STACK:
# Stack stores INDICES of days we haven't found a warmer day for yet.
# Stack stays in decreasing temperature order (monotonic decreasing).
# For each new day at index i:
#   While stack is not empty AND temperatures[i] > temperatures[stack.top]:
#     This new day is the answer for stack.top.
#     answer[stack.pop()] = i - stack.top_index
#   Push current index i onto stack.
# Any indices left in stack at the end → no warmer day → answer stays 0.
#
# WHAT IS A MONOTONIC STACK?
# A stack where elements are always in sorted order (here: decreasing temps).
# You pop whenever the order would be violated. This lets you process "waiting" indices.
#
# MEMORY HOOK: "push indices. when warmer day arrives, pop and compute the gap."

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    pass  # ← YOUR CODE HERE


# ──────────────────────────────────────────────────────────────────
# 34. NEXT GREATER ELEMENT I  (LeetCode 496)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Stack — monotonic stack + hash map
# Big O: Time O(n + m)  |  Space O(n)
#
# WHAT AM I GETTING?
# nums1: a subset of nums2 (no duplicates).
# nums2: the full array to search in.
# Find the next greater element for each value in nums1 as it appears in nums2.
#
# WHAT AM I SUPPOSED TO DO?
# For each value in nums1, find the first value to its RIGHT in nums2 that is larger.
# Return -1 if no such value exists.
# nums1=[4,1,2], nums2=[1,3,4,2] → [-1,3,-1]
# (4 has nothing greater after it in nums2; 1 has 3; 2 has nothing)
#
# THE THINKING — PRECOMPUTE ANSWERS FOR nums2, THEN LOOK UP:
# Use monotonic stack to compute next_greater for every element in nums2.
# Store in a dict: value → next_greater_value.
# For each value in nums1, look up the dict.
#
# HOW TO BUILD THE DICT WITH A STACK:
# Walk nums2. Stack holds values waiting for their next greater.
# For each new num: while stack not empty AND num > stack.top:
#   next_greater[stack.pop()] = num
# Push num onto stack.
# Remaining in stack → -1.
#
# MEMORY HOOK: "precompute next greater for all of nums2 using a stack. then look up nums1."

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    pass  # ← YOUR CODE HERE


# ──────────────────────────────────────────────────────────────────
# 35. EVALUATE REVERSE POLISH NOTATION  (LeetCode 150)
# ──────────────────────────────────────────────────────────────────
# QUESTION TYPE: Stack — expression evaluation
# Big O: Time O(n)  |  Space O(n)
#
# WHAT AM I GETTING?
# An array of tokens representing an expression in Reverse Polish Notation (RPN).
# Tokens are numbers or operators: +, -, *, /
# ["2","1","+","3","*"] → ((2+1)*3) = 9
# ["4","13","5","/","+"] → (4+(13/5)) = 6
#
# WHAT IS REVERSE POLISH NOTATION (RPN)?
# Operators come AFTER their operands, not between them.
# No parentheses needed — the order itself determines precedence.
# "2 1 +" means "2 + 1". "4 13 5 / +" means "4 + (13/5)".
#
# THE THINKING — STACK EVALUATION:
# Walk through tokens:
# If it's a number → push it onto the stack.
# If it's an operator → pop top two numbers, apply operator, push result.
# At the end, the stack has exactly one number — the answer.
#
# IMPORTANT — DIVISION:
# Problem says truncate toward zero, not floor division.
# In Python: use int(a / b), NOT a // b.
# int(-7/2) = -3 (truncate toward zero). (-7)//2 = -4 (floor, wrong for negatives).
#
# ORDER MATTERS: first pop is the RIGHT operand, second pop is the LEFT.
# b = stack.pop(), a = stack.pop() → then compute a op b.
#
# MEMORY HOOK: "number → push. operator → pop two, compute, push result. one left at end."

def evalRPN(tokens: list[str]) -> int:
    pass  # ← YOUR CODE HERE


# ══════════════════════════════════════════════════════════════════
# CHECKS — ALL AT THE BOTTOM
# Run: python notebook2_problems_21_to_35.py
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


print("\n── Q21 : Product Except Self ────────────────")
try:
    check("basic",         productExceptSelf([1,2,3,4]),   [24,12,8,6])
    check("with zero",     productExceptSelf([0,1,2]),     [2,0,0])
except: skip("not solved yet")

print("\n── Q22 : Valid Sudoku ───────────────────────")
try:
    board_valid = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    check("valid board",   isValidSudoku(board_valid),     True)
    board_invalid = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    check("invalid board", isValidSudoku(board_invalid),   False)
except: skip("not solved yet")

print("\n── Q23 : Rotate Image ───────────────────────")
try:
    m = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(m)
    check("3x3",           m,                              [[7,4,1],[8,5,2],[9,6,3]])
    m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(m2)
    check("4x4",           m2,                             [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
except: skip("not solved yet")

print("\n── Q24 : Spiral Matrix ──────────────────────")
try:
    check("3x3",           spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
    check("1x4",           spiralOrder([[1,2,3,4]]),               [1,2,3,4])
except: skip("not solved yet")

print("\n── Q25 : Reverse Linked List ────────────────")
try:
    head = make_list([1,2,3,4,5])
    check("basic",         list_to_array(reverseList(head)),  [5,4,3,2,1])
    head2 = make_list([1,2])
    check("two nodes",     list_to_array(reverseList(head2)), [2,1])
except: skip("not solved yet")

print("\n── Q26 : Merge Two Sorted Lists ─────────────")
try:
    l1 = make_list([1,2,4]); l2 = make_list([1,3,4])
    check("basic",         list_to_array(mergeTwoLists(l1, l2)), [1,1,2,3,4,4])
    check("empty lists",   list_to_array(mergeTwoLists(None, None)), [])
except: skip("not solved yet")

print("\n── Q27 : Linked List Cycle ──────────────────")
try:
    # Build 3→2→0→-4→(back to 2) manually
    n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2
    check("has cycle",     hasCycle(n1),                    True)
    check("no cycle",      hasCycle(make_list([1,2])),      False)
except: skip("not solved yet")

print("\n── Q28 : Remove Duplicates from LL ─────────")
try:
    check("basic",         list_to_array(deleteDuplicates(make_list([1,1,2]))),       [1,2])
    check("multi dups",    list_to_array(deleteDuplicates(make_list([1,1,2,3,3]))),   [1,2,3])
except: skip("not solved yet")

print("\n── Q29 : Remove Nth From End ────────────────")
try:
    check("basic",         list_to_array(removeNthFromEnd(make_list([1,2,3,4,5]), 2)), [1,2,3,5])
    check("remove head",   list_to_array(removeNthFromEnd(make_list([1,2]), 2)),        [2])
except: skip("not solved yet")

print("\n── Q30 : Intersection of Two Lists ──────────")
try:
    # Build intersecting lists manually: A=4→1→8→4→5, B=5→6→1→8→4→5
    shared = make_list([8, 4, 5])
    headA = ListNode(4); headA.next = ListNode(1); headA.next.next = shared
    headB = ListNode(5); headB.next = ListNode(6); headB.next.next = ListNode(1); headB.next.next.next = shared
    check("intersects",    getIntersectionNode(headA, headB), shared)
    check("no intersect",  getIntersectionNode(make_list([1,2,3]), make_list([4,5])), None)
except: skip("not solved yet")

print("\n── Q31 : Valid Parentheses ──────────────────")
try:
    check("simple",        isValid("()"),         True)
    check("mixed",         isValid("()[]{}"),     True)
    check("wrong order",   isValid("(]"),         False)
    check("nested",        isValid("{[]}"),        True)
except: skip("not solved yet")

print("\n── Q32 : Min Stack ──────────────────────────")
try:
    ms = MinStack()
    ms.push(-2); ms.push(0); ms.push(-3)
    check("getMin -3",     ms.getMin(),            -3)
    ms.pop()
    check("top after pop", ms.top(),               0)
    check("getMin -2",     ms.getMin(),            -2)
except: skip("not solved yet")

print("\n── Q33 : Daily Temperatures ─────────────────")
try:
    check("basic",         dailyTemperatures([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
    check("descending",    dailyTemperatures([30,40,50,60]),             [1,1,1,0])
except: skip("not solved yet")

print("\n── Q34 : Next Greater Element ───────────────")
try:
    check("basic",         nextGreaterElement([4,1,2],[1,3,4,2]),        [-1,3,-1])
    check("basic 2",       nextGreaterElement([2,4],[1,2,3,4]),          [3,-1])
except: skip("not solved yet")

print("\n── Q35 : Evaluate RPN ───────────────────────")
try:
    check("addition",      evalRPN(["2","1","+","3","*"]),               9)
    check("division",      evalRPN(["4","13","5","/","+"]),              6)
    check("negative div",  evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)
except: skip("not solved yet")

total = passed + failed
print(f"\n{'='*52}")
print(f"  SOLVED : {passed} passed / {total} attempted  |  {skipped} not yet written")
if failed == 0 and passed > 0:
    print("  All solved problems passing. Keep going.")
elif failed > 0:
    print(f"  Fix the {failed} failing test(s).")
print('='*52)