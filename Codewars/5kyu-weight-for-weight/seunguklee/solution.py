def sum_of_digits(n1):
    return sum(map(int, str(n1)))

def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split(' ')), key=sum_of_digits))