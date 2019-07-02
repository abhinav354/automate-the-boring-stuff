def collatz(number):
    if number % 2 == 0:
        x = number // 2
        return x
    elif number % 2 == 1:
        y = 3*number + 1
        return y

value = int(input('Enter any integer: '))

def retry(value):
    if collatz(value) != 1:
        r = collatz(value)
        print('It is only ' + str(r) +'. Trying again!')
        retry(r)
    elif collatz(value) == 1:
        print('1! Hallelujah! It works.')

retry(value)
    
