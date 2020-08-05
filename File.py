file = open('emilytest.txt','w')

file.write('This is a test')

read_file = open('emilytest.txt','r')

save = read_file.read()

print(save)

read_file.close()


f = open('emilytest.txt','a')
f.write('I am Jeannie')
f.close