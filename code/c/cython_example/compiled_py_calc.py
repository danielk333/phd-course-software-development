def calc(vec, mat, repeat):
    n = len(vec)
    m = len(mat)
    ret = [0] * m
    tmp = [0] * m

    for row in range(m):
        ret[row] = vec[row]
    for ind in range(repeat):
        for row in range(m):
            val = 0
            for col in range(n):
                val += ret[col] * mat[row][col]
            tmp[row] = val
        for row in range(m):
            ret[row] = tmp[row]

    return ret
