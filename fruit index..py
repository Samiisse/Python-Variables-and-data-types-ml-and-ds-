# fruit list index
fruit_list = ['Apple', 'Banana', 'Mango', 'pineapple', 'papaya']

first_fruit = fruit_list[0]
second_fruit = fruit_list[2]
third_fruit = fruit_list[3]

print(first_fruit,second_fruit,third_fruit)
print(fruit_list[1:4])

fruit_list.append('grapes') #append is to add to the list
print(fruit_list)

fruit_list.extend(['kiwi', 'Watermelon']) #extend is to extend the list before
print(fruit_list) # fruit_list.extend('Watermelon') results in  'W', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n' in the fruit_list
#make sure when extending the list you are extending to the list you have added to before like this: fruit_list.extend(['grapes', 'Watermelon'])

del fruit_list[0]
print(fruit_list) #to delete an item from the list, so we deleted index 0 which is 'Apple'

fruit_list.remove ('Watermelon') #to fremove an item, make to spell it correctly!
print(fruit_list)

print(fruit_list.pop(3))
print(fruit_list) #.pop to remove an item. In this case 'papaya is gone

fruit_list.reverse()
print(fruit_list) #it reverese the order backwards: from ['Banana', 'Mango', 'pineapple', 'grapes', 'grapes'] 
# to ['grapes', 'grapes', 'pineapple', 'Mango', 'Banana'] 

print(fruit_list)

