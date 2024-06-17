def levenshtein_distance(source, target):
    distance_matrix = [[0] * (len(target) + 1) for _ in range(len(source) + 1)]

    for c in range(len(target) + 1):
        distance_matrix[0][c] = c
    for r in range(len(source) + 1):
        distance_matrix[r][0] = r

    for r in range(1, len(source) + 1):
        for c in range(1, len(target) + 1):
            del_cost = distance_matrix[r-1][c] + 1
            ins_cost = distance_matrix[r][c-1] + 1
            if (source[r-1] == target[c-1]):
                sub_cost = distance_matrix[r-1][c-1]
            else:
                sub_cost = distance_matrix[r-1][c-1] + 1

            distance_matrix[r][c] = min(del_cost, ins_cost, sub_cost)

    return distance_matrix[len(source)][len(target)]


if __name__ == "__main__":
    # Question 4 multiple-choice
    print(levenshtein_distance("hola", "hello"))
