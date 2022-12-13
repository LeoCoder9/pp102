import os
import shutil

path1 = "documents"
path2 = "documents2"



print(os.listdir(path1))

for i in os.listdir(path1):
    
    root , ext = os.path.splitext(i)

    source = f'documents1/{root}.py'

    print(root)
    print(ext)
    
    if root == "file1":
        shutil.move(source, path2)
        
       

   
   


  

