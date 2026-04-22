def print_star_pyramid(rows):
    """
    Prints a full star pyramid pattern.

    Args:
        rows (int): The number of rows in the pyramid.
    """
    for i in range(1, rows + 1):
        # Print leading spaces for alignment
        # The number of spaces decreases as the row number increases
        print(" " * (rows - i), end="")

        # Print stars
        # The number of stars increases by 2 in each subsequent row
        print("*" * (2 * i - 1))

# Example usage:
num_rows = 5
print_star_pyramid(num_rows)