#import sys
#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
import getopt
import sys
import os

key = os.environ.get("SUPER_SECRET")
print(key)
key = os.environ.get("APP_SECRET")
print('sdfsdfds'+key)
for q in (os.getenv("APP_SECRET")):
          print(q)

# first =""
# last =""
# argv = sys.argv[1:]
# try:
#     options, args = getopt.getopt(argv, "f:l:",
#                                ["first =",
#                                 "last ="])
# except:
#     print("Error Message ")
 
# for name, value in options:
#     if name in ['-f', '--first']:
#         first = value
#     elif name in ['-l', '--last']:
#         last = value
 
# print(first + " " + last)
