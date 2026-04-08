# Lab 04: Loops and Functions Practice
# Student Name: Zuheib Abdirahman
# Date: 02/14/26

# Question 1: Robot Return to Origin


def robot_returns_to_origin(moves):
    x = 0
    y = 0
    
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        elif move == 'L':
            x -= 1
    
    return x == 0 and y == 0

test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

print("=" * 50)
print("Question 1: Robot Return to Origin")
print("=" * 50)

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))

print()


# Question 2: Two Sum

# Part A: Brute Force with Nested Loops
def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None

# Part B: Optimized with Dictionary
def two_sum_optimized(numbers, target):
    seen = {}
    
    for i in range(len(numbers)):
        needed = target - numbers[i]
        if needed in seen:
            return (seen[needed], i)
        seen[numbers[i]] = i
    return None

# Test cases for Q2
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 8, 2], 10)
]

print("=" * 50)
print("Question 2: Two Sum")
print("=" * 50)

print("=== Part A: Brute Force (Nested Loops) ===")
for numbers, target in test_cases:
    result = two_sum_brute_force(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()

print("=== Part B: Optimized (Dictionary) ===")
for numbers, target in test_cases:
    result = two_sum_optimized(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()


# Question 3: Shuffle the Array

def shuffle_array(nums, n):
    first_half = nums[:n]    # elements from index 0 to n-1
    second_half = nums[n:]   # elements from index n to end
    
    result = []
    for i in range(n):
        result.append(first_half[i])
        result.append(second_half[i])
    
    return result

# Test cases for Q3
test_cases_q3 = [
    ([2, 5, 1, 3, 4, 7], 3),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4),
    ([1, 1, 2, 2], 2)
]

print("=" * 50)
print("Question 3: Shuffle the Array")
print("=" * 50)

for nums, n in test_cases_q3:
    print("Original: " + str(nums))
    print("n = " + str(n))
    print("First half (nums[:" + str(n) + "]): " + str(nums[:n]))
    print("Second half (nums[" + str(n) + ":]): " + str(nums[n:]))

    result = shuffle_array(nums, n)
    print("Shuffled: " + str(result))
    print()


# Question 4: First Unique Character
def count_characters(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

# Main function: Find first unique character
def first_unique_character(s):
    char_counts = count_characters(s)
    
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i
    
    return -1

# Test cases for Q4
test_strings = ["leetcode", "loveleetcode", "aabb", "python", "aabbcc"]

print("=" * 50)
print("Question 4: First Unique Character")
print("=" * 50)

for s in test_strings:
    index = first_unique_character(s)
    
    if index != -1:
        print("First unique character in '" + s + "': index " + str(index) + " (character: '" + s[index] + "')")
    else:
        print("First unique character in '" + s + "': index -1 (no unique character)")
    
    counts = count_characters(s)
    print("  Character counts: " + str(counts))
    print()
    