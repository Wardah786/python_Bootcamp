user = ["Hello World\n" * 4]
for str in user:
    print(str)

print("Hello World\n" * 4, end="")

print((99 ** 3) * 8)

computer_brand = "HP"
print(f"I have a {computer_brand} computer.")

name = "Wardah"
age = 35
shoe_size = 37
info = f"Hello,I'm {name}, and I'm {age} years, I'd like a {shoe_size} shoe size please."
print(info)


a = 5
b = 2
if a > b:
    print("Hello World")


user = int(input("Guess the number, even or Odd ?"))
if user % 2 == 0:
    print(f"{user} is even.")
else:
    print(f"{user} is odd.")

user_name = input("What's your name: ")
my_name = "Warou"

if user_name == my_name:
    print("OMG, We're twinning!!")

user_height = int(input("Please insert your height here in inch : "))
if user_height > 145/2.24:
    print("Ok, you can ride")
else:
    print(user_height + "? Oh sorry, you need to grow some more")




