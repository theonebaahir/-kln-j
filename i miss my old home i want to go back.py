# Function to print a mirrored right-angled triangle
def print_mirrored_triangle(rows):
    for i in range(1, rows + 1):
        # Print spaces first
        print(" " * (rows - i), end="")
        # Print asterisks
        print("*" * i)

# Get number of rows from user
try:
    rows = int(input("Enter the number of rows for the triangle: "))
    if rows <= 0:
        print("Please enter a positive number.")
    else:
        print_mirrored_triangle(rows)
except ValueError:
    print("Please enter a valid integer.")