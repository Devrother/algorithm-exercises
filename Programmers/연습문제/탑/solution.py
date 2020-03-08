def solution(heights):
    return [check_received_tower(heights[:index], height)
        for index, height in enumerate(heights)
    ]


def check_received_tower(heights, sended_tower_height):
    for index in range(len(heights) - 1, -1, -1):
        if sended_tower_height < heights[index]:
            return index + 1
    return 0
