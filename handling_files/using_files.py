my_file = open('xment.txt', 'w+')
my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
])

#other way to read file
my_file.seek(0) #change the current file position to 0
print(my_file.read())

my_file.close()

#my_file = open('xment.txt', 'r')
#print(my_file.read())
#my_file.close()