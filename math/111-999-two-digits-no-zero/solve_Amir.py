
def MadeOfJustTwoNumbersOneToNine(number : int)->bool:
    dic = {}
    for char in str(number):
        dic[char] = '0'
    return True if len(dic) == 2 and '0' not in dic else False

cntr = 1
for i in range(112, 999):
    if MadeOfJustTwoNumbersOneToNine(i):
        print(cntr , i)
        cntr += 1
