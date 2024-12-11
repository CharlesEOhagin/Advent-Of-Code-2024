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
def sum(list1, list2):
    total = 0
    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])
    return total
print(sum(list1,list2))
def sum2(list1, list2):
    total = 0
    for i in range(len(list1)):
        list1[i]
        for j in range(len(list2)):
            count = 0
            if list2[j] == list1[i]:
                count += 1
            total += count * list1[i]
    return total
print(sum2(list1,list2))
