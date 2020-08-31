import sys

print(sys.argv)
my_str = sys.argv[1]
result = ""
for i in range(0, len(my_str), 4):
    integer = ""
    sub_str = my_str[i:i+4]
    for ch in sub_str:
        integer = hex(ord(ch))[-2:] + integer
    if len(sub_str) < 4:
        for j in range(4 - len(sub_str)):
            integer = "00" + integer
    integer = integer + "h"
    result = "push " + integer + "\n" + result
if not (len(sub_str) % 4):
    result = "push 0\n" + result

print(result)
