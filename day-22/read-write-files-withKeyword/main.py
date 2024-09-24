file = open("my_file")
contents=file.read()
#print(contents)
file.close()

#opening file with keyword
with open('my_file') as file:
    #contents=file.read()
    print(contents)
#writing into file
with open('my_file', mode='a') as file:
    file.write("\n lets continue with today's learning task")