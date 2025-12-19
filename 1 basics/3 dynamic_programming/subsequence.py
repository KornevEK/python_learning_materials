def LCS(a, b):
    # Longest common subsequence finding algorithm

    m = [[''] * (len(a) + 1) for _ in range((len(b) + 1))]

    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            if a[i-1] == b[j-1]:
                m[i][j] = m[i - 1][j - 1] + a[i-1]
            else:
                if len(m[i - 1][j]) > len(m[i][j - 1]):
                    m[i][j] = m[i - 1][j]
                else:
                    m[i][j] = m[i][j - 1]

    return m[len(b)][len(a)]

print(LCS("abac", "bcac"))

