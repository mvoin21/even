number_list = input()
number_list = b.split(',')
d = []
for item in c:
    if int(item) % 2 == 0:
        d.append(item)
print(d)

#simple
c = [int(item) for item in d if int(item) % 2 == 0]
 for item in d:
     print(d)

#simple2
number_list = input()
number_list = number_list.split(',')

def number_is_even(number):
    return int(number) % 2 == 0

for item in list(filter(number_is_even, number_list)):
    print(item)