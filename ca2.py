def is_narc(n):
    """Check if a number is narc."""
    num_str = str(n)
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == n

def print_narcis_numbers(start, end):
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1):
        if is_narc(num):
            print(num)

print_narcis_numbers(1000, 5000)
"""Submit your response here: https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u """


# Added colon on line 1 and line 10
# Changed == to = on line 3 and line 4
# Changed *** to ** on line 6
# Changed (start end) to (start, end) on line 10
# Added colon on line 12 and line 13
# Changed 'is_narcissistic' to 'is_narc' on line 13
# Changed 'print_narc_numbers' to 'print_narcis_numbers' on line 16
