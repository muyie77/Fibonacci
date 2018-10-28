def startingNumber(start = int(input("Starting number: "))):
    default = 0
    return default, start

def fibonacci(terms = int(input("Number of terms: "))):
    left, right = startingNumber()
    lst = []

    for i in range(terms):
        lst.append(right)
        for j in lst:
            print(f"{j}", end = ' ')

        print('\n')
        left, right = right, left + right



fibonacci()
