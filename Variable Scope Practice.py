#Variable Scope
#Outside the Function
total = 10

def add_nums(arg1, arg2):
    # Inside the Function
    total = arg1 + arg2
    print (total)

add_nums(3,3)
print (total)

add_nums(total, 2)
