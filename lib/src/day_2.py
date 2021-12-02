filename = "../../assets/day_2.txt"

content = open(filename).readlines()

instructions = [line.split() for line in content]

horizontal = 0
depth = 0

for command, value in instructions:
    unit = int(value)
    if (command == "forward"):
        horizontal += unit
    elif (command == "up"):
        depth -= unit    
    elif (command == "down"):
        depth += unit   

print("1. Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?")
print(horizontal * depth) 
print()        

horizontal = 0
depth = 0
aim = 0

for command, value in instructions:
    unit = int(value)
    if (command == "forward"):
        horizontal += unit
        depth += unit * aim
    elif (command == "up"):
        aim -= unit    
    elif (command == "down"):
        aim += unit   


print("2. Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?")
print(horizontal * depth) 
