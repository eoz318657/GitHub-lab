def calculate_median(numbers):
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    # Check if the length is odd or even
    if n % 2 == 1:
        # Odd case: return the middle element
        median = sorted_numbers[n // 2]
    else:
        # Even case: return average of two middle elements
        middle1 = sorted_numbers[(n // 2) - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2

    return median


# Example usage:
numbers = [5, 2, 1, 4, 3]
print("Median:", calculate_median(numbers))  # Output: 3

numbers = [1, 3, 4, 2]
print("Median:", calculate_median(numbers))  # Output: 2.5
