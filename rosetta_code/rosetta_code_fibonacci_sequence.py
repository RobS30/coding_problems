# Write a function to generate the nth Fibonacci number.
# The nth Fibonacci number is given by:
# Fn = Fn-1 + Fn-2
# The first two terms of the series are 0 and 1.
# Hence, the series is: 0, 1, 1, 2, 3, 5, 8, 13...



def fibonacci(n):
    
    #first two numbers in the fibonnaci sequence
    f = [0,1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]




if __name__ == "__main__":
    print("I should return 2")
    print(fibonacci(3))
    print("I should return 5")
    print(fibonacci(5))
    print("I should return 55")
    print(fibonacci(10))