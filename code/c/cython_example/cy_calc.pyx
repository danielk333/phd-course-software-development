def calc(vec, mat):
    cdef int n, m, val

    n = len(vec)
    m = len(mat)
    ret = [0] * m
    for row in range(m):
        val = 0
        for col in range(n):
            val += vec[col] * mat[row][col]
        ret[row] = val
    return ret
