name = input('Enter a string: ')
print(name)
num_one = input('Enter number one: ')
print(num_one)
num_two = input('Enter number two: ')
print(num_two)
if int(num_one) in range(len(name)) and int(num_two) in range(len(name)):
    print(name[int(num_one):int(num_two)])
else:
    print('Enter any number between {}'.format(range(len(name))))


