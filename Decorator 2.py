# Example 2:

# traditional way of making decorator:
def outer(fun):
    def nowexec():
        print("Executing now...")
        fun()
        print("Execution completed.")
    return nowexec

def greet():
    print("hello welcome everyone.")

a = outer(greet)                    # we can replace these two lines with @dec1, working is same.
a()

# new way of creating decorator with @.
# def outer(fun):
#     def nowexec():
#         print("Executing now...")
#         fun()
#         print("Execution completed.")
#     return nowexec
# @outer
# def greet():
#     print("welcome to everyone.")

# greet()