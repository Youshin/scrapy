# print("hello")

# text = "hello"

# print(text)

list1 = []

list1.append("hello")
list1.append("world")
#list1.append("python")

# print(list1)



def print_all():
    list2 = ""
    for i in range( len(list1) ):
        list2 = list2 + list1[i]
    print(list2)

if( len(list1) >= 3 ):
    print_all()
else:
    print("length is not enough")