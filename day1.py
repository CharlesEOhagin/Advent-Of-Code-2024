file = open("day1.txt", "r")
filecontent = file.readlines()
file.close()
list1 = []
list2 = []
for string in filecontent:
    split = string.split()
    for i in range(len(split)):
        if i == 0:
            list1.append(int(split[i]))
        else:
            list2.append(int(split[i]))
list1.sort()
list2.sort()
sum = 0
for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])
print(sum)