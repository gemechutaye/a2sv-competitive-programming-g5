if __name__ == '__main__':
    n = int(input())
    
    if n not in range(1,21):
        print("n must be inclusively between 1 and 20")
        exit() 
    
    for i in range(n):
        print(i**2)