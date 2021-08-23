# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    dimes = 0
    nickles = 0
    pennies = 0
    dimes = money // 10
    money = money % 10
    nickles = money // 5
    money = money % 5
    pennies = money
    return dimes, nickles, pennies


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
