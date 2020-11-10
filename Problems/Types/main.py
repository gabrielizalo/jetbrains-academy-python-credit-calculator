# import sys
#
# args = sys.argv
if len(args) == 5:
    arg_1 = int(args[1])
    arg_2 = int(args[2])
    arg_3 = int(args[3])
    arg_4 = int(args[4])
    my_list = [arg_1, arg_2, arg_3, arg_4]
    print(my_list)
else:
    print("The number of passed arguments is incorrect. ")
