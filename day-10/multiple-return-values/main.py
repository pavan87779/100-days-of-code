#functions with outputs

def format_name(fname,lname):
    if fname=="" or lname=="":
        return ("You not entered anything")
    format_f_name=fname.title()
    format_l_name=lname.title()
    return f"{format_f_name} {format_l_name}"

print(format_name(input("What is your first name? "), input(("What is your last name? "))))

