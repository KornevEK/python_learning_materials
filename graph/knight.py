def does_index_exist(i, j):
    if 0 <= i < len(isWin):
        if 0 <= j < len(isWin[i]):
            return True
    return False


if __name__ == "__main__":

    N, M = map(int, input().split())

    isWin = [[False for i in range(M)] for j in range(N)]

    maxDim = max(N, M)
    for sumInd in range(N + M - 2, -1, -1):
        for k in range(maxDim):
            i = k
            j = sumInd - k
            if does_index_exist(i, j):
                p1 = True
                p2 = True
                if does_index_exist(i+1, j+2):
                    p1 = isWin[i+1][j+2]
                if does_index_exist(i+2, j+1):
                    p2 = isWin[i+2][j+1]
                isWin[i][j] = not (p1 and p2)

    if isWin[0][0]:
        print("YES")
    else:
        print("NO")

