def factorial(n):
    if n < 2:
        return n
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    for i in range(0, 15 ,2):
        print(i,"! = ", factorial(i))

    
