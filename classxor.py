class passwordsdonotmatch(Exception):
    def __init__(self, message="Passwords do not match"):
        self.message = message
        super().__init__(self.message)
class passwordvalidator:
    def __init__(self,password1,password2):
        self.password1 = password1
        self.password2 = password2
    def validate_password(self):
        t=0
        try:
          for x in self.password1:
            if  int(ord(x) ^ ord(self.password2[t]))==0:
              t+=1
              continue
            else:
             raise passwordsdonotmatch()
        except passwordsdonotmatch as e:
          print(f"{e.message}")
        except Exception as e:
          print(f"{e.message}") 
        else:
          print("Passwords match")
passwordvalidator("password123", "password123").validate_password()


  
 