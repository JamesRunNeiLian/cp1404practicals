#Quick program 1
out_file = open("name.txt","w")
name = input(f"enter your name:")
out_file.write(name)
out_file.close()

#Quick program 2
in_file = open("name.txt","r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}! ")

#Quick program 3
with open ("numbers.txt","r") as number_file:
    first_number = int(number_file.readline())
    second_number = int(number_file.readline())
    result = first_number + second_number
print(result)

#Quick program 4
total = 0
with open ("numbers.txt","r") as number_file:
    for line in number_file:
        total +=int(line.strip())
print(total)
