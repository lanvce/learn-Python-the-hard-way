the_count=[1,2,3,4,5]
fruits=['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']

#this fruit kind of fora-loop goes through a list

for number in the_count:
    print(f"this is count {number}")


#same as above

for fruit in fruits:
    print(f"A fruit of type :{fruit}")

#also we can go through mixed lists too
#noticed we have to use {} since we don't know what's in it

for i in change:
    print(f"I go {i}")


#we can built lists,first start with an emoty one

elements=[]

#then use the range function to da 0 to 5 counts

for i in range(0,6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)


#now we can print them out too



for i in range(1,100,10):
    print(f"they are {i}")
    elements.append(i)


elements.append('kugou')
elements.append('wangyiyun')

del elements[10]
print (elements)
print(len(elements))
#for i in elements:
#    print(f"Elements was :{i}")
print(elements.count(1))


elements.reverse()
print (elements)
