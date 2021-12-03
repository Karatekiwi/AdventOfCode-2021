def get_bit_list(input):
    return [[int(y[x]) for y in input] for x in range(len(input[0]))]


filename = "../../assets/day_3.txt"

content = open(filename).read().splitlines()

gamma_rate = ""
epsilon_rate = ""

bit_list = get_bit_list(content)

for bits in bit_list:
    count_0 = bits.count(0)
    count_1 = bits.count(1)

    most = "0" if count_0 >= count_1 else "1"
    least = "1" if count_0 >= count_1 else "0"

    gamma_rate += most
    epsilon_rate += least

gamma_rate_num = int(gamma_rate, 2)
epsilon_rate_num = int(epsilon_rate, 2)

result = gamma_rate_num * epsilon_rate_num

print("1. Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)")
print(result) 
print()        

oxy_rating = ""
co2_rating = ""


