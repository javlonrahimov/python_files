file1 = open('f.txt', 'r')
line = file1.read()

numbers = [int(i) for i in line.split(", ")]

file2 = open('g.txt', 'w')
for number in numbers:
	file2.write(str(number) + ", ")
file2.close()