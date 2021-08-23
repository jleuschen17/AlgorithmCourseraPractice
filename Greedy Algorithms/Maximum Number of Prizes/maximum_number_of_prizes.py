# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    i = 1
    k = 0
    while n > 0:
        summands.append(i)
        n-=i+1
        k+=1
        i+=1
    summands[-1] = summands[-1] + n + i - 1
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
