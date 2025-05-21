# Task1: Read a File and Handle Errors

file1=open('sample1.txt','w')
writing_file=file1.write('Line 1: this is a sample text file.\nLine 2: It contains multiple lines.')
print(writing_file)
file1.close()

try:
    file1=open('sample1.txt','r')
except FileNotFoundError:
    print('Error: The File sample1.txt was not found.')
print(file1.read())
file1.close()



