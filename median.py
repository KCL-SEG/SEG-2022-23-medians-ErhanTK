"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

if len(numbers) % 2 != 0:
    midl_sorted = sorted(numbers)
    midl_index = (len(midl_sorted)) // 2
    median = midl_sorted[midl_index]
else:
    sorted_numbers = sorted(numbers)
    mid_index1, mid_index2 = len(sorted_numbers) // 2 - 1, len(sorted_numbers) // 2
    median = (sorted_numbers[mid_index1] + sorted_numbers[mid_index2]) / 2  # Average of two middle elements

print("Median:", median)
