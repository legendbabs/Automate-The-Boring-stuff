import random
import pprint

name = ['Tunde', 'Muhamed', 'Tolulope', 'Monsurot']

numbers = '1 2 3 4 5 6 7 8 9 0 a b c d e f g h i j k l m n o p q r s t u v w x y z \
A B C D E F G H I J K L M N O P Q R S T U  V W X Y Z'
num_list = numbers.split()
print(num_list)

# leader = random.choice(name)
# num_ = random.sample(num_list, 16)
# new_num_ = ''.join(num_)
# print(num_)
# print(new_num_)
# print(leader)

print()
random.shuffle(num_list)
# pprint.pprint(num_list)

random.shuffle(name)
print(name)