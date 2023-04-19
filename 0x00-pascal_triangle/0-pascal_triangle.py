def pascal_triangle(n):
    if n <= 0:
        return []

    result = [[1]]

    for i in range(1, n):
        new_row = [1]
        for j in range(len(result[i - 1]) - 1):
            new_row.append(result[i - 1][j] + result[i - 1][j + 1])
        new_row.append(1)
        result.append(new_row)

    return result

