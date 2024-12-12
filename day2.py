file = open("day2ex.txt", "r")
filecontent = file.readlines()
file.close()
reports = []
for string in filecontent:
    report = string.split()
    report = [int(x) for x in report]
    reports.append(report)
def safe_unsafe(report):
    differnce_list = []
    for i in range(1, len(report)):
        differnce = report[i] - report[i-1]
        if abs(differnce) > 3 or differnce == 0:
            return False
        differnce_list.append(differnce)
    same_differ = [x for x in differnce_list if x > 0]
    if (len(same_differ) != 0 and len(same_differ) != len(differnce_list )):
        return False
    return True
safety_list = []
for report in reports:
    safety_list.append(safe_unsafe(report))
def get_unsafe_list(reports, safe_list):
    unsafe_list = []
    for i in range(len(safe_list)):
        if safe_list[i] == False:
            unsafe_list.append(reports[i])
    return unsafe_list

def dampner(report):
    count = 0
    for i in range(1,len(report)):
        differnce = report[i] - report[i-1]
        if abs(differnce) > 3 or differnce == 0:
            count+=1
            count_updated = True
        
            
    return True

def get_safe(safety_list):
    count = 0
    for report in safety_list:
        if report == True:
            count += 1
    return count
print(get_safe(safety_list))
        
    