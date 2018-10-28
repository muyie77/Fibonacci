print("Starting number: ", end = '')
start = int(input())
print("Number of terms: ", end = '')
terms = int(input())

def fibonacci(num, terms):
    left = 0
    right = 1
    answer = [num]

    print(answer[0])

    formula = left + num

    answer.append(formula)
    print(f"{answer[0]}, {answer[1]}")

    while len(answer) != terms:
        formula = answer[left] + answer[right]
        answer.append(formula)
        left += 1
        right += 1
        sequence = ', '.join(map(str, answer))
        print(sequence)


fibonacci(start, terms)
