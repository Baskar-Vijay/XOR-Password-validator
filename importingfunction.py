from passwordvalidator import validate_password
import hashlib
passwordhash="ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
inputpassword=input("Enter your password: ")
hashed_input=hashlib.sha256(inputpassword.encode()).hexdigest()
validate_password(hashed_input, passwordhash)