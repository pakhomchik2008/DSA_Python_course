#dict() constructor

my_dict = dict()
print(my_dict)

my_dict2 = {}
print(my_dict2)

#same thing
# time complexity - O(1)
# Space complexity - O(1)


eng_sp = dict(one='uno',two='dos',three='tres')
print(eng_sp) #{'one': 'uno', 'two': 'dos', 'three': 'tres'}

eng_sp1 = {'one':'uno','two':'dos','three':'tres'}
print(eng_sp1) #{'one': 'uno', 'two': 'dos', 'three': 'tres'}


eng_sp3 = [('one','uno'), ('two','dos'),('three','tres')]
#time complexity ---> O(n)
#space complexity ---> O(n)


my_list_of_tuples = [('key','value1'),('key2','value2'),('key3','value3')]
print(my_list_of_tuples)
my_dict = dict(my_list_of_tuples)
print(my_dict)
