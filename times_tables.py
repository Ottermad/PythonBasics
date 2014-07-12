# times_tables.py

# Function for times tables
def times_tables(how_far, num):
    n = 1
    while n <= how_far:
        print(n, " x ", num, " = ", n*num)
        n = n + 1

# Get user's name
name = input("Welcome to Times Tables. What is your name?\n")
print("Hello " + name)

# Get timestable and how far do you want to go
times_table = int(input("Which times table to you want to know?\n"))
how_far = int(input("How far do you want to go?\n"))

times_tables(how_far, times_table)

print("Goodbye " + name + ". Thank you for playing. \nPress RETURN to exit.")

