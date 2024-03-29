# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
term = 0
num1, num2 = 0, 1
while term < 50:
    if term < 2:
        print(f'term: {term}/ number: {term}')
    else:
        sum = num1 + num2
        print(f'term: {term}/ number: {sum}')
        num1 = num2
        num2 = sum
    term += 1

# for term in range(0, 50):