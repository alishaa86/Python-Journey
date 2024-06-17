# try:
#     a = int(input("enter number: "))
#     print(a+3)

# except Exception as e:
#     print("some errors",e)


#   FILE HANDLING

s = "Hi I am Alisha and I am learning Python"
with open("test.txt", "w") as f:
    f.write(s)

