new_file=open('New_File.txt','x')
new_file.close()

import os
print("Checking if my_file.txt exists or not...")
if os.path.exists("my_file.txt"):
    os.remove("my file.txt")
else:
    print("The file does not exists.")

    my_file=open("my_file.txt","w")
    my_file.write("Hi I am a mermaid")
    my_file.close