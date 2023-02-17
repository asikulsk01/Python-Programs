from math import sqrt

# code to find all the factors of the number excluding the number itself
def factors(n):
    # vector to store the factors
    v = []
    v.append(1)

    # note that this loop runs till sqrt(n)
    for i in range(2, int(sqrt(n)) + 1, 1):

        # if the value of i is a factor
        if (n % i == 0):
            v.append(i);

            # condition to check the divisor is not the number itself
            if (int(n / i) != i):
                v.append(int(n / i))

    # return the vector
    return v


# Function to check if the number is abundant or not
def checkAbundant(n):
    sum = 0

    # find the divisors using function
    v = factors(n)

    # sum all the factors
    for i in range(len(v)):
        sum += v[i]

    # check for abundant or not
    if (sum > n):
        return True
    else:
        return False


# Function to check if the number is semi-perfect or not
def checkSemiPerfect(n):
    # find the divisors
    v = factors(n)

    # sorting the vector
    v.sort(reverse=False)
    r = len(v)

    # subset to check if no is semiperfect
    subset = [[0 for i in range(n + 1)]
              for j in range(r + 1)]

    # initialising 1st column to true
    for i in range(r + 1):
        subset[i][0] = True

    # initialing 1st row except zero position to 0
    for i in range(1, n + 1):
        subset[0][i] = False

    # loop to find whether the number is semiperfect
    for i in range(1, r + 1):
        for j in range(1, n + 1):

            # calculation to check if the number can be made by summation of divisors
            if (j < v[i - 1]):
                subset[i][j] = subset[i - 1][j]
            else:
                subset[i][j] = (subset[i - 1][j] or
                                subset[i - 1][j - v[i - 1]])

    # if not possible to make the number by any combination of divisors
    if ((subset[r][n]) == 0):
        return False
    else:
        return True


# Function to check for weird or not
def checkweird(n):
    if (checkAbundant(n) == True and
            checkSemiPerfect(n) == False):
        return True
    else:
        return False


# Driver Code
if __name__ == '__main__':
    n = int(input("Enter any number to test: "))

    if (checkweird(n)):
        print("Weird Number")
    else:
        print("Not Weird Number")
