# Write a function that calculates the total duration of the dream based on the input dream segments and returns it as a string in the format "HH:MM"
# eg: if the input dream segments are ["02:30 - 03:15",
# "03:00 - 04:00", "05:45 - 06:30"], The function should return "02:15" because the total duration of the dream is 2 hours and 15 minutes.

def dream(lst):
    num = 0
    for i in lst:
        temp = i.split("-")
        temp1 = temp[0].split(":")
        temp2 = temp[1].split(":")
        num+=(60-int(temp1[1]))+(int(temp2[1]))
    print(num)
    hour = (num//60)
    minutes = num - (hour*60)
    return "{} hours and {} minutes".format(hour,minutes)

print(dream(["02:30 - 03:15",
"03:00 - 04:00", "05:45 - 06:30"]))