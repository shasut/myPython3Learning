# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#%%
# while statement
x=2
y=4
a,b=1,5
print(a)

cond =0
while cond < 10:
    #print(cond)
    cond += 2

# infinite loop    
#while True: 
#   pass    # must press ctrl+c in the console to quit the program

#%%      
# if else statement

if a < b:
    print('a({})) is less than b({})'.format(a,b))
else:
    print('b({})) is less than a({})'.format(b,a))

print('a is less than b' if a<b else 'a is bigger than b')    

#%%
## fibonacci series
a1, b1 = 1, 1
while b1 < 50:
    print(b1)
    a1, b1 = b1, a1+b1
    
print ("Done!")

print("This line has no new line in the end = ", end='')
print("This line will be printed along with the previous line!")


#%%
## for loops





#%%
#strings

'hello'
'This a string'
"This is double quoted string"
print ('I\'m allright!')
print('This is an Example')
print("This is an Example 2")
print(21.9916/7) 
exampleVar = print('whoa')
exampleVar2 = "Hello World"
print(exampleVar2)
exampleVar2
#exampleVar


#%%
# to check length of the string
len("Hare Krishna Hare Krishna Krishna Krishna Hare Hare Hare Rama Hare Rama Rama Rama Hare Hare")


## indexing string varialble

exampleVar2[1]      # first letter
exampleVar2[-1]     # last letter
exampleVar2[:-1]    # everything except the last letter
exampleVar2[::1]    # every letter in one increment
exampleVar2[::2]    # every letter in two increment
exampleVar2[::-1]   # print backword
#exampleVar2[0]='K'
exampleVar2+"and hello universe"

print("abc"+"def") # concatenated without space
print("abc","def") # concatenated with a space

exampleVar2 = exampleVar2 + " and hello universe"
print(exampleVar2)


#%%
# string multiplication
letterVar= 'z'
letterVar=letterVar*5
print(letterVar)

# string functions
mahaVar = "Hare Krishna Hare Krishna Krishna Krishna Hare Hare Hare Rama Hare Rama Rama Rama Hare Hare"
print(mahaVar.upper())
print(mahaVar.lower())
print(mahaVar.split())



#%%
# print formatting

print('Floating point numbers: %1.2f' %(13.144))    # 2 decimal to print
print('Floating point numbers: %1.0f' %(13.144))    # 0 decimal to print
print('Floating point numbers: %1.3f' %(13.144))    # 3 decimal to print


#%%
# lists

listVar=[1,3,5]
listVar2=[1, 'Name of the list', 2.433, 'f']

print('lenght of listVAr2', len(listVar2))


## list indexing
print(listVar2[1])
print(listVar2[1:])
print(listVar2[:4])

listVar2=listVar2+['newItem']
#print(listVar2)

print(listVar2*2)   # multiplies a list

listVar.append(7)   # insert an element at the end
listVar.pop(1)      # removes an element at the given index

print(listVar)
print(listVar.pop())
print(listVar)


#%%
newListVar1=[1,4,1,9,22,3,45,23,7]
newListVar2=['a', 'e', 'c', 'l', 'u', 'b']
#print(newListVar1.reverse())

newListVar2.reverse()
newListVar2.sort()
print(newListVar2)

# https://docs.python.org/3/tutorial/datastructures.html

# del function to delete a 
del newListVar2[2]
print(newListVar2)


#%%
# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

print(matrix)


matrix1 = [
    [1, 2, 3],
    [5, 6, 7],
    [9, 1, 8],
]


print(matrix1[0][:])


#%% Dictionaries




## empty dictionaries
dictEmptyVar={}
dictEmptyVar['daughter']='One'
dictEmptyVar['sister']='two'
dictEmptyVar['marriage']='one'
dictEmptyVar['occupation']='engineer'

print(dictEmptyVar)




dictVar = {'Shaon':31,'Suthrdhar':11,'Saha':32, 'Bithi':23}
print(dictVar['Bithi'])
#print(dictVar)


dictVar['daughter']='second'
print(dictVar)

del dictVar['daughter']


#%%
# dictionaries with several values and accessing with index

dictVar2 = {'Shaon':[31, 'PhD Student', 'devotee'], 'Bithi':[23, 'sradhavan', 'comilla bari', 'Bachelor', 'BSc CSE'], 'Ahana':[18, 'Spanish'] }
print(dictVar2['Bithi'][:])
print(dictVar2['Bithi'][0])
print(dictVar2['Bithi'][1])
print(dictVar2['Bithi'][2])

## few methods for dictionaries
print(dictVar2.keys())
print(dictVar2.values())
print(dictVar2.items())


#%% Tuples
## Tuples are immutable meaning they can not be changed. 
## Useful in cases such as days of the week, or dates on a calendar.

## similar to list
## but we cannot change any value of the tuple


listVar5=[1,2,3]        # list
tupleVar5=(1,2,3)       # tuples


print(len(tupleVar5))       # returns the length
print(tupleVar5.index(1))   # return the index of the item '1'
print(tupleVar5.count(2))   # return the number of count of the item '1'



#%% Files
## reading


myfile=open('data.txt')
printVal=myfile.read()

print('first read', '\n', printVal, '\n\n')

# but second time reading will start from where
# it left it's cursor in the data.txt

printVal=myfile.read()
#print('second read',printVal)   ## it will print nothing

## to solve this we use a special method
myfile.seek(0)              # to go to the start of the file
#printVal=myfile.read()
#print('thrid read',printVal)


## the following method will make a list of all lines
print(myfile.readlines(0))
myfile.seek(0)              # to go to the start of the file
print(myfile.readlines(0))



#%% Files
## writing

myfileWrite = open('write.txt','w+')
myfileWrite.write('This is a new line\n')
myfileWrite.write('This is an another new line')
myfileWrite.seek(0)      # to go to the start of the file

printVal=myfileWrite.read()

print(printVal, '\n\n')
printVal=myfileWrite.close()


## iterating through every line in the file
myfileOpen = open('data.txt')
for readLineVar in myfileOpen:
    print(readLineVar)

myfileOpen.close()
#myfileOpen.detach()


#%% set
## Sets are an unordered collection of unique elements

setVar = set()
setVar.add(1)
setVar.add(4)
setVar.add(3)
setVar.add(2)   # this will not insert the element
setVar.add(6)
setVar.add(6)   # this will not insert the element
setVar.add(1)   # this will not insert the element
setVar


listSetVar=[1,3,4,22,44,35,23,12,22,44,1,2,3]
setVar2=set(listSetVar)
listSetVar
setVar2

#%% Comparison 

2 != 1
2 < 1
1 < 2 < 3
1 < 3 > 2

#%%

















