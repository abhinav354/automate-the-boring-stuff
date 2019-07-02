# all my cats
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop): ')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are: ')
for name in catNames:
    print('  ' + name)
    
------------------------------------------------------------------------------------------------------------------------------
# my pets
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet')

------------------------------------------------------------------------------------------------------------------------------
#comma code
spam = ['apples', 'bananas', 'tofu', 'cats']
def listwriter(list):
    list2 = list[0:-1]
    str = ''
    for i in list2:
        str += i + ', '
    str += 'and ' + list[-1]
    return str
print(listwriter(spam))

------------------------------------------------------------------------------------------------------------------------------
#character picture grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in grid:
    str = ''
    for x in i:
        str += x
    print(str)
