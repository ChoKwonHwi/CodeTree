a = input()

binary_list = list(str(a))
num = 0

if '0' not in binary_list :
    binary_list[-1] = '0'
    for i in range(len(binary_list)):
        num = num * 2 + int(binary_list[i])
    print(num)
    exit()
for i in range(1, len(binary_list)) :
    if binary_list[i] == '0' :
        binary_list[i] = '1'
        break
for i in range(len(binary_list)):
    num = num * 2 + int(binary_list[i])
print(num)
