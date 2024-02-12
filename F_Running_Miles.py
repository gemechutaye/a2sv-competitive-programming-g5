def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        prev = 0
        sorted_flag = True
        for _ in range(n):
            x = int(input())
            if prev > x:
                sorted_flag = False
            prev = x
        
        result = sorted_flag or k > 1
        print("YES" if result else "NO")

if __name__ == "__main__":
    main()
