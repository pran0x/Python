# Find the Runner-Up Score!
#! https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    #code start form here
    arr = list(set(arr))
    list.sort(arr, reverse=True)
    print(arr[1])