#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# if for loop encounters with 'break' keyword before 'else' then statement under else block won't work.

# Example 1:
fastfood = ["dosa","momo","noodles","manchuriyan","biryani"]
for item in fastfood:
    if item == "manchuriyan":
        break
    print(item)
else:
    print("these are not healthy food.")

# Example 2:
healthyfood = ["apple","rice","dal","salad"]
for item in healthyfood:
    if item == "noodles":
        break
    print(item)
else:
    print("your item is not in the list.")


