# Import necessary modules
import secrets
import string

print("""
+-------------------------+
|Random Password Generator|
+-------------------------+
      """)

# Define the alphabet
letters = string.ascii_letters 
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# Ask for the length of the password
pwd_length = int(input("Please enter password lenght: ")) 

#Generate Random Password
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print(f"""Your password is:
      🔐 {pwd}
Save it in a secure place.🚨""")
