# MyMagic8Ball

import random

# write answers
ans1 = "Yes"
ans2 = "No"
ans3 = "Maybe so"
ans4 = "Of course"
ans5 = "You crazy"
ans6 = "It is a possiblilty"
ans7 = "Do it"
ans8 = "Don't do it"

print("Welcome to MyMagic8Ball!")

# get the user's question
question = input("Ask me for advice then press RETURN to shake me.\n")
print("shaking ...\n" * 4)

# use the randint() function to select the correct answer
choice = random.randint(1, 8)

if choice == 1:
    answer = ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4
elif choice == 5:
    answer = ans5
elif choice == 6:
    answer = ans6
elif choice == 7:
    answer = ans7
else:
    answer = ans8

# print the answer to the screen
print(answer)

input("\n\nPress the RETURN key to finish.")
