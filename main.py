# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
first_digit_as_str = position[0]
second_digit_as_str = position[1]

first_digit_as_int = int(first_digit_as_str) - 1    #Represents column
second_digit_as_int = int(second_digit_as_str) - 1  #Represents row

#Replace the emoji string to 'X'
map[second_digit_as_int][first_digit_as_int] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")