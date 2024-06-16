# Simple approach using max() function and list slicing
def sliding_window(num_list: list, k: int):
    output_list = []
    for i in range(len(num_list) - k + 1):
        max_in_range = max(num_list[i:i+k])
        output_list.append(max_in_range)

    return output_list


if __name__ == "__main__":
    # Question 1 multiple-choice
    output = sliding_window([3, 4, 5, 1, -44, 5, 10, 12, 33, 1], 3)
    print(output)
