if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = sorted(set(list(arr)))
    print(a[-2])
    
    