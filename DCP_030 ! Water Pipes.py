"""
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map
where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second,
and 3 in the fourth index (we cannot hold 5 since it would run off to the left),
so we can trap 8 units of water.
"""


def water_area(elevation_map):
    # Time: O(n), Space: O(1)
    total_water_area = 0
    if len(elevation_map) < 3:
        return total_water_area

    block_space = 0

    max_high = 0
    max_high_pos = 0
    high = 0
    low = 4564416
    for index, tower_height in enumerate(elevation_map):
        if tower_height >= high:
            total_water_area += (index - max_high_pos - 1) * min(tower_height, max_high) - block_space
            high = tower_height
            if high > max_high:
                max_high = high
                max_high_pos = index
            block_space = 0
            low = high
        else:
            low = min(low, tower_height)
            block_space += tower_height
            high = tower_height

    return total_water_area


print(water_area([1, 2, 3, 4, 5, 6, 7, 50, 7, 3, 5]))

"""
while pos < len(elevation_map):
    if elevation_map[pos] >= prev_high_tow_height:
        prev_high_tow_height = elevation_map[pos]
        prev_high_tow_pos = pos
    else:
        low = elevation_map[pos]
        break
    pos += 1
"""