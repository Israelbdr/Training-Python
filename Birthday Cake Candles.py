
# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    height = ar[0]
    candlesblown=0
    for i in range(len(ar)):
        if ar[i]>height:
            height=ar[i]
    for i in range(len(ar)):
        if ar[i]==height:
            candlesblown+=1
    return(candlesblown)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
