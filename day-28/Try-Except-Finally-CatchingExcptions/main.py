try:
    file=open("file.txt")
    a_file={"key":"value"}
    print(a_file["key"])
except FileNotFoundError:
    file=open("file.txt", "a")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content=file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")