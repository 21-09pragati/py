fruits=['apple','watermelon','mango','cherry','guava','watermelon','banana']
rollno=[212,43,211,434,112,767,876]
# print(fruits[3])

# print(fruits[2:5])

# print(fruits.index('guava'))

# print(len(fruits))

# print(fruits.count('watermelon'))

# print(fruits.index('pear'))                         #error_type{item is not in list}
# print(fruits[7])                                    #error_type{list index out of range}

# fruits.sort()                                       #ascending order
# print(fruits)

# fruits.reverse()                                    #after sorting apply reverse function to print the list in descending order
# print(fruits)

# print(min(fruits))
# print(max(rollno))
# print(sum(rollno))

# print(fruits.append('strawberry'))                 #this will print none as print functin and string function does not work at a time as append only add element at the end but does not update the list
# fruits.append('strawberry')

# print(fruits)
# fruits.insert(1,'grapes')                          #add element to specific index
# print(fruits)
# print(fruits)

# fruits[1]='raspberry'                             # 1 will get replace by another value
# print(fruits)
# fruits.extend(rollno)                             #to append lists

# fruits.remove('watermelon')                        #it will remove first element from list which is duplicate 
# print(fruits)

# fruits.pop()                                      #it will remove last element from list ans also can mention specific index
# print(fruits)
# print(fruits)

# fruits.pop(3)
# print(fruits)



# Q.Selling lemonade
# You sell lemonade over two weeks, the lists show number of lemonades sold per week
# Profit for each lemonde sold is 1.5$
# Add another day to week 2 list by capturing a
# number as input Combine the two lists into the list called 'sales'
# Calculate/ print how much you have earned on
# Best day
# Worst day
# Separately and in total
# #Hint: 3 prints in total
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales =[]
new_w1=input("Enter number of lemonade sales for last day: ")
sales_w2.append(int(new_w1))
sales.extend(sales_w1)
sales.extend(sales_w2)
sales.sort()
worst_day_prof=sales[0]*1.5
best_day_prof=sales[-1]*1.5
print(f'Worst day profit is $ {worst_day_prof}') 
print(f'best day profit is $ {best_day_prof}')
print(f'Combined best day and worst day profit {worst_day_prof+best_day_prof}')