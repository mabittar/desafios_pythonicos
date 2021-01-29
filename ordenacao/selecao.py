def insert(L):
    n = len(L)
    for i in range(0, n-1):
        x = L[i]
        j = i
        while j >= 0 and L[j] > x:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = x
