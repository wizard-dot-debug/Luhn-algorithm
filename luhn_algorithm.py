def luhn_algorithm(a):
    revesed_a = a[::-1]
    odd_a = revesed_a[::2]
    sum_of_odd_a = 0
    for i in odd_a:
        sum_of_odd_a += int(i)
        
    even_a = revesed_a[1::2]
    sum_even_a = 0
    for j in even_a:
        seccond_digits = int(j)*2
        if seccond_digits >=9:
            seccond_digits -= 9
            sum_even_a += seccond_digits
        else:
            sum_even_a += seccond_digits
            
    total = sum_even_a + sum_of_odd_a
    return total % 10

print()
print('Welcome To Luhn Algorithm.')
print()

x = input('Give Your Card Number: ')

def str_convert(a):
    y = str.maketrans({'-':'', ' ':''})
    covert_a = a.translate(y)
    if luhn_algorithm(covert_a) == 0:
        return 'VALID!'
    else:
        return 'INVALID!'

print(str_convert(x))

