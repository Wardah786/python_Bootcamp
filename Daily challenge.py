user_word = input("Please enter a string: ").strip()
list_of_characters_without_duplicates = [user_word[0]]
for char_idx in range(1, len(user_word)):
    if user_word[char_idx] is not user_word[char_idx-1]:
        list_of_characters_without_duplicates.append(user_word[char_idx])
print(" ".join(list_of_characters_without_duplicates))


user_string = input("please input a word: ").strip()
"".join(set(user_string))
print(user_string)



