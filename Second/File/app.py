
with open('Second/File/data.txt','r') as file:
 file_content=file.read()
 print(file_content)
          
with open('Second/File/data2.txt','w') as file:
 file.write(file_content)      
          