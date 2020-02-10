from tajribe import suml,prodl

# in case the module and the python file isn't in the same folder
# from sys import path
# path.append('..\\modules')
#import tajribe
# or you can add the path in this way
#path.append('C:\\Users\\user\\py\\modules')
# Or
#path.insert('C:\\Users\\user\\py\\modules')

# to surf between python programs we just use the name of the folder
#example: extra.good.best.tau.funT()

zeroes = [ 0 for i in range(5)]
ones = [1 for i in range (5)]
print(suml(zeroes))
print(prodl(ones))