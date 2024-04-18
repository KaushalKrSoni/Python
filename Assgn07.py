def factorial():
    n=10
    i=n
    if n<0:
        print(f"factorial of negative number is not possible")

    elif n==0:
        return 1

    else:
        for n>=0:
            for i>=0:
                factorial=factorial*n
                i=i-1
            return factorial

factorial()