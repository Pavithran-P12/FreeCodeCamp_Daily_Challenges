from collections import Counter  # Import Counter, a dict subclass for counting hashable objects

def find_duplicates(nums):
    # Count occurrences of each number in the input list
    counts = Counter(nums)
    # Create a list of numbers that appear more than once
    duplicates = [num for num, count in counts.items() if count > 1]
    # Return the sorted list of duplicate numbers
    return sorted(duplicates)



def find_duplicates_no_counter(nums):
    seen = set()
    # Create a set to keep track of numbers we've already seen
    duplicates = set()
    # Create a set to store numbers that are duplicates
    for num in nums:
        # Iterate through each number in the input list
        if num in seen:
            # If the number is already in 'seen', it's a duplicate
            duplicates.add(num)
            # Add the duplicate number to the 'duplicates' set
        else:
            seen.add(num)
        # If the number is not in 'seen', add it to 'seen'
    return sorted(duplicates)
    # Return the sorted list of duplicate numbers

# Example usage:
# print(find_duplicates_no_counter([4, 3, 2, 7, 8, 2, 3, 1]))  # Output: [2, 3]
