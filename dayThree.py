#!/usr/bin/python

#tuples

#Empty Tuples

tup1=()

#Create tuple with one element
tup2=(2,)


print tup1

print tup2

tup3=(1,2,3,4,5,"hello",5)

#to find the count of 5
#Everything in python is treated as object . object.function()
count=tup3.count(5)
print ("occurence of 5 is:")
print count

#find index of 5

loc=tup3.index(5)

print("index of 5 is")
print loc

#for i,j print upto i to j-1
tupSlice=tup3.__getslice__(2,5)

print("Tuple Element between 2 to 5")
print(tupSlice)

#del(tup3)
#tuple already deleted ,hence cant be accessed
print(tup3)


#merge two tuples
tup4=tup2+tup3
print("After merging tup2 and tup3")
print tup4

#will overwrite the element in list but not in tuples
#tup4[4]="11"

#print tup4


#accessing all elements in tuples
#iterator is tup4 here 
for t1 in tup4:
    if t1==5:
        print "element found",t1

#2nd wayof accessing using index

tupLen=len(tup4)
i=0
while i<tupLen:
    print tup4[i]
    i=i+1


#dictionary 

#key value 

dict1={}

dict1['ip1']="192.168.1.0"
dict1['ip2']="192.168.1.1"
dict1['ip3']="192.168.1.2"


print dict1

for keys in sorted(dict1.iterkeys()):

    print dict1.get(keys)


print("2nd way of dict print")

print dict1['ip3']

#Sets 
#Unordered Collection
#doesnt allow duplicate element

set1={"area1","area1","area3"}

print len(set1)

set1.add("area4")

print set1
#doesnt support indexing 
#print set1[0]

#union and intersection of sets

set2={"area4","area6","area7","area8"}

set3=set1.union(set2)
print set3

#intersection

set4=set1.intersection(set2)

print("intersection result")
print set4


#1 Enter two numbers from argument and multiply them and print result
#2 Enter two strings from console and concatenate them and print result
#3 Enter 5 elements from argument and store in a list list1 and append a new value and print result
#4 From the above list find the element between 2nd and 5th index
#5 Check whether 2 is present orr not in the list 
#6 Check whether tuple can add a new element 
#7 Using for loop create a new dictionary of 10 elements which contains number as keys and its square as values i.e dict[2]=4
#8 Using a set create a union of 2 sets first set containing area and second set containing Zip code
#9 Convert from binary to decimal using Python literals i.e 1010 = 10
#10 Concatenate a number and a string i.e Hello and 9 result hello9


