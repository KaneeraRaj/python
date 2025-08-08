file_read=open('codingal.txt', 'r')
print("File in Read Mode-")
print(file_read.read())
file_read.close  

file_write=open('codingal.txt','w')
file_write.write("File in the write mode")
file_write.write("hi i am penguin and i am ten years old")
file_write .close