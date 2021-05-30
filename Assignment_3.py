#%%
# Dictionary Questions
# Q.1 Write a Python Program to sort (ascending and descending) a dictionary by value.
# Ans.1
temp_dict={1:4, 10:1, 2:2, 5:1, 8:3}
print("Ascending order of values")
print(sorted(temp_dict.items(), reverse=False, key=lambda dic:(dic[1],dic[0])))

print("Descending order of values")
print(sorted(temp_dict.items(), reverse=True, key=lambda dic:(dic[1],dic[0])))
# %%
# Q.2 Write a Python Program to add a key to a dictionary. 

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# Ans.2
dict1={0:10, 1:20}
key, value=map(int, input().strip().split(" "))
dict1[key]=value
print(dict1.items())
# %%
# Q.3 Write a  program asks for City name and Temperature and builds a dictionary using that Later on you can input City name and it will tell you the Temperature of that City.
# Ans.3
temperature={}
flag=True
while(flag):
    city, temp=input().split()
    temperature[city]=temp
    ans=input("Want to enter more? y/n")
    flag=(ans=="y")
print(temperature.items())

city=input("Enter city name: ")
if(city in temperature.keys()):
    print(city+":"+temperature[city])
# %%
# Q.4 Write a Python program to convert list to list of dictionaries.

# Sample lists: ["Black", "Red", "Maroon", "Yellow"], 
# ["#000000", "#FF0000", "#800000", "#FFFF00"]

# Expected_Output=[{'color_name': 'Black', 'color_code': '#000000'},
# {'color_name': 'Red', 'color_code': '#FF0000'}, 
# {'color_name': 'Maroon', 'color_code': '#800000'},
# {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
# Ans.4
color=["Black", "Red", "Maroon", "Yellow"]
hex_code=["#000000", "#FF0000", "#800000", "#FFFF00"]
list_of_dict=list()
for c, h in zip(color, hex_code):
    d={'color_name':c, 'color_code':h}
    list_of_dict.append(d)
print(list_of_dict)
# %%
# Q.5 We have following information on Employees and their Salary (Salary is in lakhs)
employee=['John', 'Smith', 'Alice', 'Daneil']
salary=[14,13,32,21]
data={}
for e, s in zip(employee, salary):
    data[e]=s

choice=input("Enter command")
if(choice=="print"):
    for emp in data.keys():
        print(emp+"==>"+str(data[emp]))
elif(choice=="add"):
    name=input("Enter the name of employee")
    if name in data.keys():
        print(name+" Already exists")
    else:
        sal=int(input("Enter salary"))
        data[name]=sal
        print("Dictionary:",data.items())
elif(choice=="remove"):
    name=input("Enter name to remove")
    if name in data.keys():
        data.pop(name)
        for emp in data.keys():
            print(emp+"==>"+data[emp])
    else:
        print(name+" doesn't exist!")
elif(choice=="query"):
    name=input("Enter name of employee")
    print(name+": "+str(data[name]))
# %%
# Set Questions
# Q.1 What is the difference between a set and a frozenset? Create any set and try to use frozenset(setname).
# Ans.1 Frozen set is just an immutable version of a set.
set1={2,1,4,7,3,10}
print(set1)
print(frozenset(set1).difference({4}))
set1.discard(4)
print(set1)
# %%
# Q.2 Find the elements in a given set that are not in another set
# Difference between set1 and set2 is {10,20,30}
set1 = {10,20,30,40,50}
set2 = {40,50,60,70,80}
print(set1-set2)
# %%
