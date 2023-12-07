#Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
def count_digit_one(n):
    count = 0
    factor = 1
    current = n // factor

    while current > 0:
        higher = n // (factor * 10)
        current_digit = current % 10
        lower = n - (current * factor)

        if current_digit == 0:
            count += higher * factor
        elif current_digit == 1:
            count += higher * factor + lower + 1
        else:
            count += (higher + 1) * factor

        factor *= 10
        current = n // factor

    return count

n = int(input())

if 0 <= n <= 109:
    result = count_digit_one(n)
    print(result)
