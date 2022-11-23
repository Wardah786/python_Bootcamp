#  Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = [30, 11, 12, 7]
my_fav_numbers.append(15)
my_fav_numbers.append(31)
my_fav_numbers.remove(7)

friend_fav_numbers = [18, 0, 2]
our_fav_numbers = my_fav_numbers + friend_fav_numbers
print(our_fav_numbers)


# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# No, tupples are immutable


# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)
basket_count = basket.count('Apples')
print(basket_count)

# Recap – What is a float? What is the difference between an integer and a float?
# a float ris not a round figure, contains decimal places, to the closest value and an integer is a number a round figure
 # using range or float itself?!!

my_lst =[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
my_lst.reverse()
print(my_lst)
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index

numbers = range(1, 21)
for number in numbers:
    if number % 2 == 0:
        print(number, end=" ")



username = ["Wardah"]
while username:
    user1 = input("Please enter the username (enter 'quit' if you don't know): ")
    if user1 == 'quit':
        username = False
    elif user1 == 'cancel':
        username = False
    elif user1 == 'stop':
        username = False
    else:
     print("Correct", username)
     break
