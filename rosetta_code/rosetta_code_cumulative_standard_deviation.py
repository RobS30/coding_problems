# Write a function that takes an array of numbers as parameter and returns the standard deviation of the series.

def standardDeviation(arr):


    # calculate the mean of the numbers in the data ou are working with
    mean = 0
    for i in arr:
        mean += i
    mean = mean / len(arr)
    
    # subtract the mean from each, then square the result
    variance = 0
    for i in arr:
        deviation = i - mean 
        dsquared = deviation**2 
        variance += dsquared

# work out the mean of the squared differences
    mean_variance = variance / len(arr)


# take the square root
    standard_deviation = mean_variance**(1/2)

    return standard_deviation



if __name__ == "__main__":
    print("I should return 2")
    print(standardDeviation([2, 4, 4, 4, 5, 5, 7, 9]))
    print("I should return 147.323")
    print(standardDeviation([600, 470, 170, 430, 300]))
    print("I should return 18.239")
    print(standardDeviation([75, 83, 96, 100, 121, 125]))
    print("I should return 16.87")
    print(standardDeviation([23, 37, 45, 49, 56, 63, 63, 70, 72, 82]))
    print("I should return 22.631")
    print(standardDeviation([271, 354, 296, 301, 333, 326, 285, 298, 327, 316, 287, 314]))