def iseven(number):
    if number % 2 == 0:
        return True
    else:
        return False


# divide watermelon in 2 parts, each of them weighing an even number
# has to be whole numbers
# does NOT have to be equal

def main():
    number = int(input())  # user input
    for i in range(2, 100, 2):  # goes through all evens
        for x in range(2, 100, 2):  # goes through all evens
            if iseven(i) and iseven(x) and (i + x) == number: # if both nums even and both nums == total then we chillin
                return "YES"
    return "NO"


# I want all even numbers that add to the number


if __name__ == "__main__":
    print(main())
    # has to be a better way to do this
