file_read=open('p.txt','r')
print("File in Read Mode..")
print(file_read.read())
file_read.close()

file_write=open('p.txt','w')

file_write.write("File in write mode...")

file_write.write("hi i am pranjala and i am 16 years old")
file_write.close

file_append=open('p.txt','a')

file_append.write("\n File in append mode...")

file_append.write("Hi I am penguin and I am twenty years old")

file_append.close()
