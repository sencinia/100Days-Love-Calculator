# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

true_count = 0

true_count += lower_name1.count("t") + lower_name2.count("t")
true_count += lower_name1.count("r") + lower_name2.count("r")
true_count += lower_name1.count("u") + lower_name2.count("u")
true_count += lower_name1.count("e") + lower_name2.count("e")

love_count = 0

love_count += lower_name1.count("l") + lower_name2.count("l")
love_count += lower_name1.count("o") + lower_name2.count("o")
love_count += lower_name1.count("v") + lower_name2.count("v")
love_count += lower_name1.count("e") + lower_name2.count("e")

love_score = int(str(true_count) + str(love_count))

if love_score < 10 and love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >40 and love_score < 50:
  print(f"Your score is {love_score}, You are alright together.")
else:
  print(f"Your score is {love_score}.")
