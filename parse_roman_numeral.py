# parse_roman_numeral.py

"""
This script defines a function to convert a Roman numeral string into its integer value.
It includes detailed comments and example usage for clarity.
"""

def parse_roman_numeral(numeral):
    """
    Convert a Roman numeral string to its integer equivalent.

    Parameters:
    numeral (str): A Roman numeral string (e.g., 'XIV', 'MCMXCIV')

    Returns:
    int: The integer value of the Roman numeral
    """
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    # Loop through the string in reverse order
    for char in reversed(numeral):
        value = roman_map.get(char, 0)
        if value < prev_value:
            total -= value  # Subtract if smaller than previous
        else:
            total += value  # Add if equal or larger
        prev_value = value

    return total

# Example usage
if __name__ == "__main__":
    test_cases = ["IV", "XL", "XC", "CD", "CM", "MCMXCIV"]
    for roman in test_cases:
        result = parse_roman_numeral(roman)
        print(f"{roman} → {result}")
