from math import sqrt

def primes_to(M):
    # Sieve of Eratosthenes
    # generate candidates
    nums = list(range(2, M))
    i = 0  # first element is prime
    while i < len(nums) and nums[i] < sqrt(M):
        # remove its multiples
        nums = list(filter(
            lambda x: (x % nums[i] or x == nums[i]),
            nums))
        i += 1  # next element is prime
    # when we reach sqrt(M), its next multiple is out of the bounds, so stop
    return nums

def primes_range(N, M):
    return list(filter(
        lambda x: x > N,
        primes_to(M)))

def is_palindrome(x):
    return str(x) == str(x)[::-1]

def palindromic_primes(N, M):
    return list(filter(
        is_palindrome,
        primes_range(N, M)))

if __name__ == "__main__":
    N = int(input("Enter the starting point N:\n"))
    M = int(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for x in palindromic_primes(N, M):
        print(x)
