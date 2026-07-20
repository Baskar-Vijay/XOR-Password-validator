import classxor
import hashlib
passwordhash="ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
inputpassword=input("Enter your password: ")
hashed_input=hashlib.sha256(inputpassword.encode()).hexdigest()
classxor.passwordvalidator(passwordhash, hashed_input).validate_password()