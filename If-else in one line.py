"""
syntax: for simple if-else

statement1 if condition_true else statement2
if the condition true then statement1 will execute else the statement2 will execute>

syntax: for nested if-else

statement1 if condition1_true else statement2 if condition2_true else statement3...so


"""

a = int(input("enter the value:"))

# simple if-else:
print("even") if a%2==0 else print("odd")

# nested if-else:
print("zero") if a == 0 else print("even") if a%2 == 0 else print("odd")
