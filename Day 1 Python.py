#!/usr/bin/env python
# coding: utf-8

# In[4]:


x = 9

y = x - 2

print(y)


# In[8]:


my_name = "Makhimba"
print(my_name)


# In[10]:


"Makhimba" = likes_
purple
print("Makhimba")


# In[11]:


likes_purple = "Makhimba"
print(likes_purple)


# In[14]:


print(likes_purple) 
print(y)


# In[16]:


row_1_column_1_book_1_title = "Pachinko"
print("Pachinko")


# In[17]:


print(row_1_column_1_book_1_title)


# In[52]:


row_1_column_1_book_1_author =" by Min Jin Lee"
print(row_1_column_1_book_1_title +
      row_1_column_1_book_1_author)


# In[27]:


cupcakes = 2 + 6 / 3
print(cupcakes)


# In[29]:


cupcakes = 6 ***2
print (cupcakes)


# In[30]:


cupcakes = 7 / 2
print (cupcakes)


# In[31]:


x = 1
print (x)


# In[33]:


x = x + 2
print (x)


# In[34]:


x = 3
print(x
    )


# In[35]:


x = 3 * 5
print (x)


# In[36]:


y = x / 3
print (y)


# In[38]:


pizza = 5 
print(pizza)


# In[39]:


y = pizza * 2
print(y)


# In[41]:


z = y / 5
print (x)


# In[42]:


w = z + 3
print (w)


# In[47]:


pizza = 5
number_eaten = 2000000000000000000000
x = pizza * number_eaten
print(x)


# In[48]:


homework = 5
finished = 3
z = (homework - finished)
print (z)


# In[49]:


print("Apple")


# In[50]:


print ("hello world")


# In[57]:


speed = 50
speed = 51
print (speed)


# In[58]:


speed = speed * 2
print (speed)


# In[61]:


first_name ="Makhimba"
last_name = "Simon"
print(first_name + " "+ 
      last_name)


# In[68]:


food = "ice cream"
sentence = "Hi, my name is"
print (sentence + " " +
       first_name + " " + last_name )


# In[73]:


x = "and my favorite food is"
print (sentence +" "+ 
       first_name + " " + last_name + " " + x + " " + food)


# In[77]:


food = "ice cream"
name = "Makhimba"
sentence = "hi my name is " + name + " and my favorite food is " + food
print (sentence)


# In[86]:


location= "Brooklyn"
Name = "Makhimba"
sentence = " hi my name is " + name + " and I live in " + location + "."
print (sentence)


# In[87]:


print (sentence + ",NY")


# In[97]:


miles = 2
sentence = ()"I ran" + " " + str(miles) + " " + "miles" 
+ ".")
print (sentence)


# In[102]:


miles = 2
sentence = "I ran" + " " + str(miles)+ " " + "miles"
print (sentence)


# In[103]:


x= 0
x>0


# In[105]:


x >= 0


# In[106]:


x==0


# In[108]:


y = 2
y==2


# In[109]:


y>0


# In[110]:


x = 5
x<y


# In[111]:


(y + 1)== (y)


# In[113]:


y=2
x=1
(x==2) or (y==2)


# In[119]:


y=2
x=1
(x==1) or (y==10)


# In[120]:


y=10
x=20
(x>5) and (y!=10)


# In[163]:


temp = 95
if temp >= 90:
    print ("its too hot!")
elif temp >= 70:
    print("its perfect")
elif temp >= 50:
    print ("its getting chilly")
elif temp <= 32:
    print ("its cold")
else:
    print("its between 32 and 50")


# In[185]:


temp = 109
if temp < 100 and temp>=80:
    print("it must be summer")
elif temp <80 and temp >= 50:
    print("it must be spring")
elif temp <50 and temp >= 32:
    print("it must be fall")
elif temp >=100: 
    print("not on earth")
else: 
    print("it must be winter!")


# In[228]:


price= 20
color = "blue"
if price >= 75:
    print(price - 10)
elif price >=30:
    print (price-5)
elif price >= 10 and color == "red":
    price=0
    print (price)
else:
    print( "no discount!")


# In[234]:


price=25
color = "red"
if price >= 10:
 if color == "red":
    price = 0
    print (price)


# In[258]:


grade=90
if grade >=90:
    print("A")
elif grade >=80 and grade <90:
    print ("B")
elif grade >70 and grade <80:
    print ("C")
elif grade <=70 and grade >0:
    print ("Please see teacher for extra credit")
else: 
    print("try again next year")


# In[291]:


Office= ["Michael", "Pam"]
if (len(Office)) >=2: 
    print("the office is full")
    print(Office[0])
elif (len(Office)) < 2:
    print("the office is empty")


# In[293]:


Office= ["Michael", "Pam"]
Office.append ("Dwight")
print(Office)


# In[308]:


Office= ["Michael","Dwight","Stanley", "Jim", "Pam"]
Office.insert(1,"Dwight")
Office.insert(3,"Jim")
print(Office)
Office.pop()
remove=Office.pop()
print(remove + " was removed from the office")


# In[326]:


Office= ["Michael","Dwight","Stanley", "Jim", "Pam"]
print(len(Office))
print(Office[2])
print(Office[3])
removed=Office.pop(0)
Office.append (removed)
print(Office)


# In[353]:


grades= [100,90,80,70,50]
print(max(grades))
remove=grades.pop ()
grades.insert(1,remove)
print(grades)
grades.append (100)
print(grades)
print (sum(grades)/len(grades))
print(grades)


# In[354]:


Office= ["Michael","Dwight","Stanley", "Jim", "Pam"]
Office[0:4]


# In[367]:


for person in Office:
    print(person)


# In[365]:


print(person)


# In[374]:


print ("taking attendance")

for person in Office:
    print( person  +  "is here")
    print("Attendence is taken")


# In[387]:


Office= ["Michael","Dwight","Stanley", "Jim", "Pam"]
for person in Office:
    print ( "hello "  +   person) 


# In[389]:


grades= [100,90,80,70,50]
for number in grades:
    print(number*2)


# In[401]:


sales = [100,200,10,50,75]
for number in sales:
    if number <= 50:
        print("You get a discount")
    elif number >50:
        print("sorry no discount")


# In[405]:


x=sales
print(type(x))


# In[409]:


sales = [100,200,"apples", 4.5,10.7,50,75]
for number in sales:
    if type(number)==float:
        print(number/2)
    else:
        print("Not a float")


# In[ ]:




