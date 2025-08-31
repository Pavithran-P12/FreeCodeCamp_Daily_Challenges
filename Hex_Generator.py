# hex_generator.py

import random

def generate_hex(color):
    """
    Generates a random 6-character hexadecimal color code where the specified
    color channel ('red', 'green', or 'blue') is dominant.

    Parameters:
        color (str): The name of the dominant color channel.

    Returns:
        str: A 6-character hex color code (e.g., "FF3A7C") or "Invalid color" if input is unsupported.
    """

    # Normalize input to lowercase for consistency
    color = color.lower()

    # Helper function to generate two random values less than 255
    def get_two_lower_channels():
        a = random.randint(0, 254)
        b = random.randint(0, 254)
        return a, b

    # Assign RGB values based on the dominant color
    if color == "red":
        # Generate green and blue channels randomly
        g, b = get_two_lower_channels()
        # Ensure red is strictly greater than both
        r = max(g, b) + random.randint(1, 255 - max(g, b))
    elif color == "green":
        r, b = get_two_lower_channels()
        g = max(r, b) + random.randint(1, 255 - max(r, b))
    elif color == "blue":
        r, g = get_two_lower_channels()
        b = max(r, g) + random.randint(1, 255 - max(r, g))
    else:
        # Handle unsupported color inputs
        return "Invalid color"

    # Format RGB values into a 6-character uppercase hex string
    return "{:02X}{:02X}{:02X}".format(r, g, b)

# Example usage
if __name__ == "__main__":
    print("Red dominant:", generate_hex("red"))
    print("Green dominant:", generate_hex("green"))
    print("Blue dominant:", generate_hex("blue"))
    print("Invalid input:", generate_hex("yellow"))
