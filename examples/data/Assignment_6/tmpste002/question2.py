""" Basic vector calculations in 3 dimensions: addition, dot product and normalization """
__author__ = 'Stephen Temple'
__date__ = '2014/04/23'


def main():
    # Define lambda functions
    add = lambda a, b: [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
    dot_product = lambda a, b: (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])
    normalize = lambda a: (a[0]**2 + a[1]**2 + a[2]**2)**(1 / 2)

    # Input each vector
    vector_a = [int(i) for i in input("Enter vector A:\n").split(' ')]
    vector_b = [int(i) for i in input("Enter vector B:\n").split(' ')]

    # Print the calculations
    print('A+B = {}'.format(add(vector_a, vector_b)))
    print('A.B = {}'.format(dot_product(vector_a, vector_b)))
    print('|A| = {0:.2f}'.format(normalize(vector_a)))
    print('|B| = {0:.2f}'.format(normalize(vector_b)))


if __name__ == '__main__':
    main()