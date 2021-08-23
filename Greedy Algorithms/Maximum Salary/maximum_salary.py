# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    numbers.sort(reverse=True)
    i = int(pow(10,  (2 * len(numbers)) - 2))
    salary = int(0)
    for number in numbers:
        salary += int(i * int(number))
        i = i // 100
    return salary



if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
