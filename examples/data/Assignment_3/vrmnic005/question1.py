def print_rectangle(height, width):
    for row in range(height):
        print("*" * width)

if __name__ == "__main__":
    height = int(input("Enter the height of the rectangle:\n"))
    width = int(input("Enter the width of the rectangle:\n"))
    print_rectangle(height, width)
