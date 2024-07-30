#Python has a set of built-in methods that you can use on lists/arrays.
#1.append:-
#ex 1:-
name = ["akash","prasad","rohan",]
print(name)

#ex 2:-
city1 =["Pune","Mumbai","kolhapur",]
city2 = ["Nashik", "Nagpur", "Solapur"]
city3 =city2.append(city2)
print(city3)

for city in city2:
    city1.append(city)
    
print(city1)   


#2.count():-
fruits = ['apple', 'banana', 'cherry','mango','watermelon','orange','apple','apple'] 
x=fruits.count("apple")
print(x)


#3.extend:-
fruits = ['apple', 'banana', 'cherry','mango','watermelon','orange']
cars   = ['Honda','Hyundai','Tata']
fruits.extend(cars)
print(fruits)

#4.pop() :-
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)
print(fruits)

