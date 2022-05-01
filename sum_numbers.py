file1 = open('f.txt', 'r')
line = file1.read()

numbers = [int(i) for i in line.split(", ")]

file2 = open('g.txt', 'w')
file2.write(str(sum(numbers)))
file2.close()