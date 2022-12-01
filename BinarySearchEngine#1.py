from bisect import bisect_left
def binarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and  a[i] == x:
        return i
    else:
        return -1
a = [63, 28, 17, 46, 19, 28, 73, 64, 98, 12, 76, 34, 98, 17, 26, 34, 98, 17, 26, 34, 98, 17, 26, 34, 98, 71, 62, 98, 37, 46, 19, 28, 73, 64, 91, 27, 63, 49, 81, 27, 63, 49, 87, 16, 23, 49, 87, 16, 29, 38, 47, 61]
x = int(87)
res = binarySearch(a, x)
if res == -1:
    print(x, "is absent")
else:
    print("First occurance of", x, "is present at", res)