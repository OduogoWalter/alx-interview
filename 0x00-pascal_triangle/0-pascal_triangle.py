#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the n-th row.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list of lists: A list of lists of ints representing Pascal's Triangle.
                       Returns an empty list if n <= 0.
    """
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle list to hold all rows
    triangle = []

    # Loop through each level of the triangle
    for i in range(n):
        # Start each row with [1]
        row = [1]

        # If we're beyond the first row, calculate the in-between values
        if i > 0:
            # Previous row for reference
            prev_row = triangle[i - 1]

            # Add the values between the starting and ending 1's
            for j in range(1, i):
                # Each element is the sum of the two elements directly above it
                row.append(prev_row[j - 1] + prev_row[j])

            # End the row with a 1
            row.append(1)

        # Append the current row to the triangle
        triangle.append(row)

    return triangle
