import os 
import shutil



print("welcome to my programming of organizer Files ")
print('''
      
Programming under processing  please wite .....      
      
      
      
      '''
      )
# this code about how you orgnazer your folder 
# current_dir=os.path.dirname(os.path.realpath(__file__))

# for filename in os.listdir(current_dir):
    
           
#     if filename.endswith((".png",".jpg",".jpeg")):
             
#         if not os.path.exists("images"):
#             os.mkdir("images")
#         shutil.copy(filename ,"images");
#         os.remove(filename)
#     print(" Images is Done ")
# print("Programing completed !!!! ")
        
       

class Organizer():
    def __init__(self):
        self.current_dir=os.path.dirname(os.path.realpath(__file__))


    
      
    
    def organizer(self):
        

        for filename in os.listdir(self.current_dir):
           
           #this code to copy files images to image folder 
            if filename.endswith(("png","jpg","gif","jpeg")):
                if not os.path.exists("images"):
                    os.mkdir("images")
                shutil.copy(filename,"images")
                os.remove(filename)
            print("Images Copy is Done  ")
            
            # this code for copy pdf and doc and excel to Folder  Doc 
            if filename.endswith(("pdf","docx","xlsx","csv","txt","xls","pptx","doc")):
                if not os.path.exists("Doc"):
                    os.mkdir("Doc")
                shutil.copy(filename,"Doc")
                os.remove(filename)
            print("Doc  Copy is Done  ")
            
            # this code for copy exe and zip files to App Folder 
            if filename.endswith(("exe","zip","msi","rar")):
                if not os.path.exists("AppFolder"):
                    os.mkdir("AppFolder")
                shutil.copy(filename,"AppFolder")
                os.remove(filename)
            print("App  Copy is Done  ")
            
            # this code copy files programming to folder Code 
            if filename.endswith((".py","css","html")):
                if not os.path.exists("code"):
                    os.mkdir("code")
                shutil.copy(filename,"code")
                os.remove(filename)
            print("Code  Copy is Done  ")
            
            # this code for copy video files to folder video 
            if filename.endswith(("mp4")):
                if not os.path.exists("Video"):
                    os.mkdir("Video")
                shutil.copy(filename,"Video")
                os.remove(filename)
            print("Video  Copy is Done  ") 
           
c1=Organizer()

c1.organizer()