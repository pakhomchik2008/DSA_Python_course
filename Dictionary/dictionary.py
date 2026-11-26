# a dictionary is a collection which is unordered,changable and indexed
# my_dict = {'miller': 'a person who owns or works in a corn mill'}
#miller - key , a person... = value

# myDict['Miller'] = a person who owns ....



#dict() constructor

# my_dict = dict()
# print(my_dict)

# my_dict2 = {}
# print(my_dict2)

#same thing
# time complexity - O(1)
# Space complexity - O(1)


# eng_sp = dict(one='uno',two='dos',three='tres')
# print(eng_sp) #{'one': 'uno', 'two': 'dos', 'three': 'tres'}

# eng_sp1 = {'one':'uno','two':'dos','three':'tres'}
# print(eng_sp1) #{'one': 'uno', 'two': 'dos', 'three': 'tres'}

#time complexity ---> O(n)
#space complexity ---> O(n)


# my_list_of_tuples = [('key','value1'),('key2','value2'),('key3','value3')]
# print(my_list_of_tuples)
# my_dict = dict(my_list_of_tuples)
# print(my_dict)

# eng_sp_list = [('one','uno'), ('two','dos'),('three','tres')]
# eng_sp3 = dict(eng_sp_list)
# print(eng_sp3)


# ------------------------- Dictionary in Memory --------------

# a hash table is a way of doing key-value lookups.
# You store the values in an array,
#  and then use a hash function to find the index of the array cell that corresponds 
# to your key-value pair

#how has function works

engToSp = {'one':'uno',}