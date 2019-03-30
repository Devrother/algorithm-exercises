def whatFlavors(cost, money):
    cash = {}
    for i, integ in enumerate(cost):
        if money - integ in cash:
            print(cash[money - integ], end=" ")
            cash[integ] = i + 1
            print(cash[integ])
        cash[integ] = i + 1


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)