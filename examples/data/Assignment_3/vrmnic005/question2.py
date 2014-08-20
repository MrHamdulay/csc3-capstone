def print_triangle(height):
    for row in range(height):
        print(" " * (height - row - 1) + "*" * (2*row + 1))

if __name__ == "__main__":
    height = int(input("Enter the height of the triangle:\n"))
    print_triangle(height)
