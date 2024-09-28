n1 = int(input('Enter your number here : '))
n2 = int(input('Enter your number here : '))
n3 = int(input('Enter your number here : '))

if n1 < n2 and n1 < n3:
    print('n1 = least value')
elif n2 < n1 and n2 < n3:
    print('n2 = least value')
elif n3 < n1 and n3 < n2:
    print('n3 is the least value')