# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d
    tank_remaining = m
    position = 0
    num_of_stops = 0
    if (d - stops[-1]) > m:
        return False
    for x in range(len(stops)):
        if stops[x] > tank_remaining + position:
            num_of_stops+=1
            position += stops[x - 1]
            x-=1
        if stops[x] == tank_remaining + position:
            num_of_stops+=1
            position += stops[x]
            x-=1
    return num_of_stops


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
