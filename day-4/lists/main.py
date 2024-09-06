#python lists is a data structure in python
fruits=["apple","banana","orange","strawberry","kiwi"]
fruits.append("mango")
print(fruits)
print(fruits[0])
print(fruits[1])
fruits.append("graphs")
print(fruits)
#accessing right to left
print(fruits[-1])
print(fruits[-2])
#changing values in list
fruits[1]="avagado"
fruits[2]="pineapple"
print(fruits)
#performing severals inbuilt operations on lists
fruits.clear()
print(fruits)
fruits.extend(["apple","banana","orange","mango","kiwi"])
print(fruits)
# inseet
fruits.insert(1,"berry")
print(fruits)
fruits.remove("apple")
print(fruits)
print(fruits.pop())