#Task2:  Write and Append Data to a file.
file1=open('output.txt','w')
write_file = file1.write('Hello Python!')
file1.close()

file1=open('output.txt','a')
append_file = file1.write('Learning file handling in Python')
file1.close()

file1=open('output.txt','r')
read_file1=file1.read()
print(read_file1)
file1.close()

