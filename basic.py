# name ="vijay"

# # print (name)

# print("kapil")

# number = 10000
# print(number)
# print(name)

# num = 12.556
# print(num)

# #>>>>>>>>>>>>
# print(5+5*10)


# >>>>>>>>>>string<<<<<<<<<<<@@@@@@@@@@@@@@@@@@@@@@@@@
# name =  "vijay" #01234
# print(name[0:2])
# print(name[0:4])
# print(name[4])

# print(name[0:5])
# print(type(name))
# num = 100.2
# print(type(num))

# print(len(name))

# na = "kapil"
# print(na)

# name = "kapil" #as a string 

# name_upper = "KAPIL" #as a string 
# print(name.upper()) # upper case 

# print(name.lower()) # lower  case  

# print(name.swapcase())
# print(name.title())
 
# print(name.replace("kapil","dim"))

# name = "kapil"
# last_name = "kumar"

# print(name+last_name)
# print(name+"  "+ last_name)

# print(name.find("k"))
# print(last_name.find("m"))

# print(name.capitalize())


# my name is kapil

# print("my namr is ",name,"and my last name is",last_name)

# print(3 *name)
# print(2*last_name)

# print(f"my name is {name} and my last_name is {last_name}")

# print(name.replace("i","j"))
# print(name.replace("i","j",1))

# text = "hello vijay"
# print(text.replace("vijay","python"))

# print(text.index("vijay"))

# >>>>>>>>>>>>list#############@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%

# my_list1 = [1,2,3,4,5,6,7,8,9]

# print(type(my_list))

# my_list = [1,"ritik",3,4.2,True,5,6,7,8,9]

# print(type(my_list))
# print(my_list)

# print(my_list)
# print(my_list[2])
# print(my_list1[5])

# my_list = [1,2,3,45,3,5,7,4,6,3,3,5,443]
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
# print(my_list[-4])
# print(my_list[-5])
# print(my_list[-6])
# print(my_list[-7])

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])
# print(my_list[6])


# my_list = [1,2,3,45,3,5,7,4,6,3,3,5,443]

# print(my_list[1:5])
# print(my_list[:5])
# print(my_list[3:8])
# print(my_list[12:])
# print(my_list[:])

# print(len(my_list))
# my_list.append(100)
# my_list.append(159)

# print(my_list)

# my_list.insert(6,134)
# print(my_list)

# my_list.remove(443)
# my_list.remove(3)
# print(my_list)

# my_list.pop()
# print(my_list)

# my_num = [5,4,3,2,1]
# # my_num.sort()
# my_num.clear()
# print(my_num)





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>tuple and dict<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#############operation of tuple 

# tpl =  (1,2,3,4,5)
# print("tpl:-",tpl)

# print("type of tpl:-",type(tpl))
# print("len of tpl:-",len(tpl))
print
# print("0 position ka element :-", tpl[0])
# print("1 position ka element :-", tpl[1])
# print("2 position ka element :-", tpl[2])
# print("3 position ka element :-", tpl[3])
# print("4 position ka element :-", tpl[4])

# print("0  to  2 position ka element :-",tpl[0:2])

# print("1 position ka element :-",tpl[::-1]) 




# tpl = (1,2,3,4,5)

# print(2 in tpl)
# print(10 in tpl)

# print("max of tpl:-",max(tpl))
# print("min of tpl:-",min(tpl))
# print("sum of tpl:-",sum(tpl))


# tpl1 = 1,2,3,54,5,4,4
# print(type(tpl1))
# print(tpl1)


##############tuple upcoming
# vijay = 1,2,3


# a,b,c = vijay
# print("a:-",a)
# print("b:-",b)
# print("c;-",c)



#######################data list dist tuple ############

# >>>>>>>>>>>>>>>>>dict<<<<<<<<<<<<<<<<<<<<<<<


# dct = {
#     "name" : "vijay",
#     "last_name" : "kumar",
#     "age" : 21  

# }

# print("dct type:-",type(dct))
# print("dct :-",dct)
      
# print(dct["name"])

# dct["gender"] = "male" #adding 
# print(dct)

# dct["class"] = 12 #adding
# print(dct)

# dct["age"] = 22 #updating
# print(dct)

# del dct['last_name']
# print(dct)

# dct.pop["last_name"]
# print(dct)

# dct.clear()
# print(dct)
# print('name' in dct)
# print('vijay' in dct)

dct = {
    "name" : "vijay",
    "last_name" : "kumar",
    "age" : 21  

}

# dct1 = dct.copy()
# print(dct1)

# copy_dct = dct.copy() #copy
# print("copy dict:- ", copy_dct)
# print("orignal dict :-",dct)




# merging distionaries



# dct1 = {
#     "vikram_name" : "vijay",

#     "vikram_age" : 21

# }


# dct2 =  {
#     "kapil_name" : "kapil",
#     "last_name" : "kumar",
#     "kapil_age" : 21
# }

# dct.update(dct2)
# print(dct1) 

# key = ("a","b","c")
# default_dict=dict.fromkeys(key,0)

# print(default_dict)######{'a': 0, 'b': 0, 'c': 0}



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>set<<<<<<<<<<<<<


# my_set = {1,2,3,4,5,"vijay"}
# print(type(my_set))

# my_set.add(100)
# my_set.add("kapil")
# my_set.add("vijay")
# print(my_set)

# my_set.discard(5)
# print("discard element:-",my_set) #pop

# my_set.pop()
# print("pop element:-",my_set)# pop

# my_set.clear()
# print("clear  element:-",my_set) #clear

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>operator<<<<<<<<<<<<<<<<<<<<<<<<<<
n = int(input('enter number :'))
i=1
while i <= 10:
    print(n*i)
    i +=1