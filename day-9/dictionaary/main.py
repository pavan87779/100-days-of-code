programming_dictionary={
    "Bug":"An error in a program that prevents the programfrom running as expected.",
    "function":"A piece of code that you can easily call over and over again",
    "loop":"The action of doing something over and over again.",

}
print(programming_dictionary["Bug"])

for key in programming_dictionary:
    print(f"{key} :")
    print(programming_dictionary[key])
