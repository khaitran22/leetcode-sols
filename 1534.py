def countGoodTriplets(arr, a, b, c) -> int:
    count = 0
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    count += 1
    return count

arr = [3,0,1,1,9,7]; a = 7; b = 2; c = 3
print(countGoodTriplets(arr,a,b,c))