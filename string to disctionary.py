temp = "555 Air India 666 Spicejet"
temp += '/'


# output will be {'555': ' Air India ', '666': ' Spicejet'}


dict ={}
j = 0
while temp[j] != "/":
    num = ''
    bank = ''
    while temp[j] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        num += temp[j]
        j += 1

    while temp[j] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']:
        bank += temp[j]
        j += 1
    dict[num] = bank[1:]
    
print(dict)
