import random
lst = [random.randint(1,100) for _ in range(10) ] 
print(lst)

lst = [i for i in range(10) if i%2==0]
print(lst)

lst1 = [
    ['城市','环比', '同比'],
    ['北京', 102, 103],
    ['上海', 101, 102],
    ['深圳',100,39]
]
for row in lst1:
    for item in row:
        print(item, end='\t')
    print()

lst2 = [ [j for j in range(4)] for i in range(4)]
print(lst2)

##aa