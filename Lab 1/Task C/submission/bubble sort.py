def bubbleSortNorm (arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            break

def bubbleSortRev (arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            break

def bubbleSortAbs (arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(0, n-i-1):
            if abs(arr[j]) > abs(arr[j+1]) or (abs(arr[j]) == abs(arr[j+1]) and arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            break

n = int (input())
arr = list(map(int, input().split()))
bubbleSortNorm(arr)
print(*arr)
bubbleSortRev(arr)
print(*arr)
bubbleSortAbs(arr)
print(*arr)