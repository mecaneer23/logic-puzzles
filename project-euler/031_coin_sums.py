#!/usr/bin/env python3

# https://projecteuler.net/problem=31

# def get_all_elements(elements: list[int], target_value: int) -> list[int]:
#     """
#     Return a list of the maximum amount of each number
#     that can add up to the target value
#     """
#     output: list[int] = []
#     for element in elements:
#         for _ in range(target_value // element):
#             output.append(element)
#     return output


def coin_sums() -> int:
    """Return the amount of ways £2 can be made using any number of coins"""
    # https://raw.org/puzzle/project-euler/problem-31/
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target_value = 200
    table = [0] * (target_value + 1)
    table[0] = 1
    for coin in coins:
        for i in range(coin, target_value + 1):
            table[i] += table[i - coin]
    return table[target_value]
    # coins = [200, 100, 50, 20, 10, 5, 2, 1]
    # all_elements = get_all_elements(coins, target_value)
    # all_elements should be changed to a dict where key=coin value
    # and value=amount_remaining
    # current: list[int] = []
    # counter = 0
    # element_index = 0
    # last_element = 0
    # while True:
    #     if last_element != 0:
    #         current.append(all_elements[all_elements.index(last_element) + 1])
    #     else:
    #         current.append(all_elements[element_index])
    #         element_index += 1
    #     if sum(current) < target_value:
    #         continue
    #     print(current)
    #     if sum(current) == target_value:
    #         counter += 1
    #         all_elements.remove(current[0])
    #         if len(set(current)) == 1:
    #             element_index = 0
    #             current.clear()
    #             continue
    #     last_element = current.pop()
    # # found: set[str] = set()
    # found = 0
    # start_index = 0
    # # current: list[int] = [0]
    # # TODO: replace len(set(current)) == 1 with is_all_same variable
    # # TODO: replace current list with current: int (sum)
    # while True:
    #     current: list[int] = []
    #     index = start_index
    #     while True:
    #         print(current)
    #         if sum(current) == target_value:
    #             print(current)
    #             found += 1
    #             if len(set(current)) == 1:
    #                 start_index += 1
    #             break
    #         if start_index == len(coins):
    #             return found
    #         current.append(coins[index])
    #         if sum(current) + coins[index] >= target_value:
    #             # raise NotImplementedError("Hmm")
    #             index += 1
    #     # while True:
    #         # current.append(coins[start_index])
    #     # while True:
    #     #     current.append(coins[index])
    #     #     if "+".join(map(str, current)) == one_string:
    #     #         return len(found)
    #     #     print(current)
    #     #     if sum(current) >= 200:
    #     #         if "+".join(map(str, current)) not in found:
    #     #             found.add("+".join(map(str, current)))
    #     #             break
    #     #         current.pop(-1)
    #     #         index = min(index + 1, len(coins) - 1)

print(coin_sums())
