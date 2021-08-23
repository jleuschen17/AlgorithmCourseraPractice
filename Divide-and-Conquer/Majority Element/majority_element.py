# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    midpoint = len(elements) // 2
    left = elements[:midpoint]
    right = elements[midpoint:]
    if len(left) > 2:
        return majority_element(left), majority_element(right)
    elif len(right) == 3:
        if right[0] == right[1] or right[0] == right[2] or right[1] == right[2] or left[0] == left[1]:
            return 1
    elif len(right) == 2:
        if right[0] == right[1] or left[0] == left[1]:
            return 1
    return 0





if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
