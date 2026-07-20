class passwordsdonotmatch(Exception):
    def __init__(self, message="Passwords do not match"):
        self.message = message
        super().__init__(self.message)
def validate_password(password, password2):
 t=0
 try:
  for x in password:
     if  int(ord(x) ^ ord(password2[t]))==0:
       t+=1
       continue
  
     else:
         raise passwordsdonotmatch()
         break
 except passwordsdonotmatch as e:
     print(f"{e.message}")
     
 else:
     print("Passwords match")
validate_password("password123", "password13")
