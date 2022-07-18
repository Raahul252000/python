# 1 method:
list1 = ["bhindi","aloo","gobhi","chopsticks","manchurian","noddles",]
# i = 1
# for item in list1:
#     if i%2 is not 0:
#         print(f"please buy {item}")
#     i +=1

# by using enumerate function:
for index,item in enumerate(list1):
    if index%2 ==0:
        print(f"hey dude!! Buy {item}")