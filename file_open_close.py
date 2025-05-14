'''
file1= open('my_file.txt','r')
#use to open a file and need to close close it
reading_file = file1.read()
print(reading_file)
file1.close()


#another way to open and edit the file
#with open('my_file.txt','w') as file1:
    #statements
'''
from fileinput import close

#add data to a file, remember it clears all the existing data in the file
'''
file1= open('my_file.txt','w')
writing_file= file1.write('Hey')
print(writing_file)
file1.close()

file1= open('my_file.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()
'''
#appending it helps us by writing in a a file without clearing its contents
'''
file1=open('my_file.txt','a')
file_writing=file1.write('\nAhoy There welcome')
#print(file_writing)#it prints the no. of statements in the file
file1.close()

file1= open('my_file.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()
'''

#read and write
file=open('my_file.txt','r+')
writing_file=file.write('Welcome here')
print(writing_file)
file.close()

file1= open('my_file.txt','r+')
reading_file = file1.read()
print(reading_file)
file1.close()