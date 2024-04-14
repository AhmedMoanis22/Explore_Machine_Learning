# => immutable

my_tuple = ("max" , 28 , "Boston")
my_tuple2 = "zedan" , "mohamed" , 21

# print(my_tuple , my_tuple2)

# my_tuple[0]= "min"

a = (1,2,3,4,5,6,7,8,9,10)

b = a[::-1]

# print(b , type(b))

name , age, city = my_tuple

# print(name , age , city)

i1,*i2,i3 = a #i2 -> list

# print(i1 , i2 , i3)


# list is large than tuple

# import sys

# lst = [1,2,3,"zedan","mohamed"]
# tpl = (1,2,3,"zedan","mohamed")

# print(sys.getsizeof(lst) ,"Bytes" , sys.getsizeof(tpl) , "Bytes")

import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5]" , number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)" , number=1000000))
