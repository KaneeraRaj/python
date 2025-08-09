with open('codingal.txt','w') as file:
    file. write("Hi i am a little mermaid")
    file.close()

with open('codingal.txt','r') as file:
 data=file.readlines()
 print("Word in this file are...")
 for line in data:
  word= line.split()
  print(word)
file.close