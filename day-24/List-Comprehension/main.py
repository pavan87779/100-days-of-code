number=[1,2,3]
new_list=[n+1 for n in number]
print(new_list)

name="pavan"
new=[letter for letter in name]
print(new)

#list comprehension in range
range_list =[num*2 for num in range(1,10)]
print(range_list)

#conditional list comprehension
list=[num*2 for num in range(1,20) if num%2==0]
print(list)

n=['pavan','babu','saan','kumar','babbi']
short_n=[name.upper() for name in n if len(n)>4]
print(short_n)