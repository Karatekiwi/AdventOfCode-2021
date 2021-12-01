
def calculate_increases(input):
    increases = 0

    for x, y in zip(input[::], input[1::]):
        if y - x > 0:
            increases += 1

    return increases

filename = "../../assets/day_1.txt"

content = open(filename).readlines()

depths = [int(depth) for depth in content]

increases = calculate_increases(depths)

print("1. How many measurements are larger than the previous measurement?")
print(increases) 
print()        
    
sums = []

for x,y,z in zip(depths[::],depths[1::],depths[2::]):
    sum = x + y + z
    sums.append(sum)

sum_increases = calculate_increases(sums)

print("2. How many sums are larger than the previous sum?")
print(sum_increases) 

