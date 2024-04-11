#removing  Letter From a String in Python
#word=("geek1fo1rge1ek")
#wordtoremove=input("")
#neword=word.replace(wordtoremove,'')
#print(neword)
#_________________________________________________________________________________________________

#ways to find length of a list
#list=[10,20,30,40,50]
#length=len(list)
#print(length)
#_________________________________________________________________________________________________
#Find Maximum of two numbers in Python usinf def  and error handling
#try:
 #   def max_min(a,b):
  #      if a>b:
   #         print(a)
    #    else:
     #       print(b)

    #num1=int(input("first num: "))
    #num2=int(input("second num: "))


    #s=(max_min(num1,num2))
    #print(s)
#except ValueError:
 #   print("only numbers can be compared")
#__________________________________________________________________________________________________
#Check if element exists in list in Python

#list=['3','sar','root','2','4','5']

#check=input()
#if check in list:
    #print("true")
#else:
 #   print("false")
#___________________________________________________________________________________
#program to print all odd numbers in a range
#start=int(input())
#end=int(input())

#for i in range(start,end+1):
 #   if i % 2 != 0:
#
#        print(i)
#________________________________________________________________________________________________-
#Python program to print positive numbers in a list
#list=[1,-1,2,-4,5,6,-77]

#for i in list:
#    if i > 0:
#        print(i)
#___________________________________________________________________________________________-____
#codechef roller coster problem
#n = int(input())

#for i in range(n):
#    X, Y = map(int, input().split())

#    if X >= Y:
#        print("yes")
#    else:
#        print("no")
#_________________________________________________________________________________________________
#codechef chef date problem
#num=int(input())
#for i in range(num):
#    x,y=map(int,input().split())
#    if(x>=y):
#        print('Yes')
#    else:
#        print('No')
#________________________________________________________________________________________________
#codechef counting word problems
#T=int(input())
#for i in range(T):
#    N,M=map(int,input().split())
#    tot=N*M
#    print(tot)
#_________________________________________________________________________________________________
#How to count unique values inside a list
#list=[1,2,3,4,4,5,5,6,6,1,2,8]
#unique_list=[]
#s=0
#for i in list:
#    if i not in unique_list:
#        s= s+1
#        unique_list.append(i)
#print(unique_list)
#print(s)
#_________________________________________________________________________________________________________
#Python – List product excluding duplicates
#list=[1,1,2,3,5,5,6,6]
#unique_list=[]
#res=1
#for i in list:
#    if i not in unique_list:
#        res = res*i
#        unique_list.append(i)
#print(unique_list)
#print(res)
#_________________________________________________________________________________________________
#Python – Test if List contains elements in Range
#try:
#    list=[1,2,3,4,5,6,7,8,9,10]
#    listneo=[]
#    a,b=map(int,input("> enter space btw range>").split())
#    c=True
#    for i in list:
#        if i<a and i>=b in list:
#            c=False
#            break
#    print(c)
#except ValueError:
#    print("enter space bar between the range that you enter")
#______________________________________________________________________________________________________________
#Handling missing keys in Python dictionaries
#try:
#    enter1=str(input("enter new key: "))
#    enter2=int(input("enter new value: "))
#    enter3=str(input("which key's value you want: "))
#    dic = {'a': 1, 'b': 2}
#    dic[enter1]=enter2

#    print(f"The value associated with {enter3} is : ")
#    print(dic.get(enter3))
#except KeyError:
#    print("you have enter wrong key or assign a value to it")
#except ValueError:
#    print("keys can only be string and values can only be integer")
#________________________________________________________________________________________________________
#Python program to find the sum of all items in a dictionary
def sum_dic(dicti):
    list=[]
    for i in dicti:
        list.append(dicti[i])
    ans=sum(list)
    return ans



dic={
    'a':1,
    'b':2,
    'c':3,
    'd':40
}
print(sum_dic(dic))
