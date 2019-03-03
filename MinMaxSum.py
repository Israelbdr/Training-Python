
# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    min=arr[0]
    max=arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        elif arr[i] < min:
            min = arr[i]
    print (sum(arr)-min)
    print (sum(arr)-max)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
