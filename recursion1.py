import random
def getAnswer(number):
    if number == 1:
        return 'It is certain'
    elif number == 2:
        return 'It is decidely so'
    elif number == 3:
        return 'Yes'
    elif number == 4:
        return 'Reply hazy, try again'
    elif number == 5:
        return 'Ask again later'
    elif number == 6:
        return 'Concentrate and ask again'
    elif number == 7:
        return 'My reply is no'
    elif number == 8:
        return 'Outlook not so good'
    elif number == 9:
        return 'Very unlikely'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
def retry():
    decision = input('Do you want to try again?')
    if decision == 'y':
        m = random.randint(1,9)
        print(getAnswer(m))
        retry()
    else:
        print('Thanks for playing')

retry()
