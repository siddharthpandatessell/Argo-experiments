file_name = 'my_file.txt'
f = open(file_name, 'w+')  # open file in write mode
f.write('python rules')
f.close()
print('The file was created successfully')