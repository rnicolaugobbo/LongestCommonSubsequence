def longest_common_subsequence(s1, s2):
    print("Finding longest commom subsequence of {0} and {1}".format(s1, s2))

    grid = [[0 for c in range(len(s1) + 1)] for c in range(len(s2) + 1)]

    for row in range(1, len(s2) + 1):
        for col in range(1, len(s1) + 1):
            if s1[col -1] == s2[row - 1]:
                grid[row][col] = grid[row - 1][col - 1] + 1
            else:
                grid[row][col] = max(grid[row - 1][col], grid[row][col -1])
    
    result = []
    while row > 0 and col > 0:
        if s1[col - 1] == s2[row - 1]:
            result.append(s1[col - 1])
            row -= 1
            col -= 1
        elif grid[row - 1] > grid[col - 1]:
            row -= 1
        else:
            col -= 1
    result.reverse()
    return "".join(result)