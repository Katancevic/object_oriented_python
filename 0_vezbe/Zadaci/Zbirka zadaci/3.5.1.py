mylist = [2,3,4,5,6,7,8,9,10]

list_new  = list(filter(lambda x : (x%2==0), mylist))

print(list_new)