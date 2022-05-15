
# if we list all of the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.  The sum of these multiples is 23.

# find the sum of all the multiples of 3 and 5 below the provided parameter value number

def multiplesOf3and5(number):
    array_of_multiples = []
    sum_of_multiples = 0 

    for i in range(number):
        if i % 5 == 0:
            array_of_multiples.append(i)
        elif i % 3 == 0:
            array_of_multiples.append(i)
    
    sum_of_multiples = sum(array_of_multiples,0)
    return sum_of_multiples



if __name__ == "__main__":
    print("Test Case 1: I should return 543")
    print(multiplesOf3and5(49))

    print("Test Case 2: I should return 233168")
    print(multiplesOf3and5(1000))
    
    print("Test Case 3: I should return 16687353")
    print(multiplesOf3and5(8456))
    
    print("Test Case 4: I should return 89301183")
    print(multiplesOf3and5(19564))
