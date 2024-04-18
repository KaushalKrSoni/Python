# n=int(input("Enter the number: "))

def fact(n):
    factorial=1
    if n<0:
        print(f"factorial of negative number is not possible")

    elif n==0:
        return 1

    else:
        while n>=0:
            factorial=factorial*n
            n=n-1
        return factorial
    

fact(5)