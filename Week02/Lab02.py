# Lab 2: Insertion Sort
# COMP2152 - Week 2
# Zuheib Abdirahman Student ID: 101549351
# Date: 2026/01/25

def insertion_sort(arr):
    """
    Sort an array using insertion sort algorithm.
    
    Parameters:
    arr (list): List of numbers to sort
    
    Returns:
    list: Sorted list in ascending order
    """
    # Make a copy to avoid modifying original
    sorted_arr = arr.copy()
    # Start from the second element (index 1)
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]  # Current element to insert
        j = i - 1            # Start comparing with previous element
        # Move elements of sorted_arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < sorted_arr[j]:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        
        # Insert the key at the correct position
        sorted_arr[j + 1] = key
    
    return sorted_arr

def test_insertion_sort():
    """Test the insertion sort function with various cases."""
    print("=== Testing Insertion Sort ===\n")
    test_cases = [
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([3, 1, 4, 1, 5], [1, 1, 3, 4, 5]),
        ([], []),
        ([1], [1]),
        ([9, 8, 7, 6, 5], [5, 6, 7, 8, 9]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])  # Already sorted
    ]
    all_passed = True
    for i, (input_arr, expected) in enumerate(test_cases, 1):
        result = insertion_sort(input_arr)
        if result == expected:
            print(f"Test {i}: PASSED ✓")
        else:
            print(f"Test {i}: FAILED ✗")
            print(f"  Input:    {input_arr}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            all_passed = False
        print()
    
    if all_passed:
        print("All tests passed! ✓")
    else:
        print("Some tests failed.")
    
    return all_passed
def interactive_demo():
    """Interactive demo for insertion sort."""
    print("\n=== Interactive Demo ===")
    print("Enter numbers separated by spaces (e.g., '5 2 8 1 9')")
    print("Press Enter with no input to exit.\n")
    while True:
        user_input = input("Enter numbers: ").strip()
        if not user_input:
            print("Exiting demo.")
            break
        
        try:
            numbers = [float(x) if '.' in x else int(x) for x in user_input.split()]
            original = numbers.copy()
            sorted_numbers = insertion_sort(numbers)
            
            print(f"\nOriginal: {original}")
            print(f"Sorted:   {sorted_numbers}")
            print("-" * 40)
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")

if __name__ == "__main__":
    print("COMP2152 - Week 2 Lab: Insertion Sort")
    print("=" * 40)
    # Run tests
    test_passed = test_insertion_sort()
    
    if test_passed:
        # Run interactive demo if tests passed
        interactive_demo()
    else:
        print("Fix the implementation before running interactive demo.")