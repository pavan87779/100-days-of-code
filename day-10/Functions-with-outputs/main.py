#functions with outputs

def format_name(fname,lname):
    format_f_name=fname.title()
    format_l_name=lname.title()
    return f"{format_f_name} {format_l_name}"

output=format_name(fname="PAVAN",lname="Babu")
print(output)

#function 1 and function 2
def function1(text):
    return text+text
def function2(text):
    return text.title()
output1=function1("hello")
output2=function2("hello")
print(output1)
print(output2)