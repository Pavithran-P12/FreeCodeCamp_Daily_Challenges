def tribonacci_sequence(start_sequence, length):
    # If requested length is 0, return empty list
    if length == 0:
        return []
    
    # Initialize result with as many items from the start sequence as needed
    result = start_sequence[:length]
    
    # Keep generating numbers until we reach the desired length
    while len(result) < length:
        # Take the last 3 elements from the sequence (result[-3:])
        # Add them together (sum(...))
        # Append this new value to the sequence (result.append(...))
        result.append(sum(result[-3:]))
    
    return result


# Example usage:
print(tribonacci_sequence([0, 0, 1], 10))  
# Output: [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]


"""
Step-by-step breakdown for tribonacci_sequence([0, 0, 1], 10):

Start: result = [0, 0, 1]

Iteration 1:
    Last 3 = [0, 0, 1], sum = 1
    Append → result = [0, 0, 1, 1]

Iteration 2:
    Last 3 = [0, 1, 1], sum = 2
    Append → result = [0, 0, 1, 1, 2]

Iteration 3:
    Last 3 = [1, 1, 2], sum = 4
    Append → result = [0, 0, 1, 1, 2, 4]

Iteration 4:
    Last 3 = [1, 2, 4], sum = 7
    Append → result = [0, 0, 1, 1, 2, 4, 7]

Iteration 5:
    Last 3 = [2, 4, 7], sum = 13
    Append → result = [0, 0, 1, 1, 2, 4, 7, 13]

Iteration 6:
    Last 3 = [4, 7, 13], sum = 24
    Append → result = [0, 0, 1, 1, 2, 4, 7, 13, 24]

Iteration 7:
    Last 3 = [7, 13, 24], sum = 44
    Append → result = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]

Done → 10 numbers generated.
"""
