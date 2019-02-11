T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    H_index = (N-1) % H + 1
    W_index = (N-1) // H + 1

    if W_index > 9:
        print(f'{H_index}{W_index}')
    else:
        print(f'{H_index}0{W_index}')

