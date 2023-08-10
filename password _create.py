from bcrypt import *
password = ""
salt = gensalt(rounds=10)
_password = hashpw(password.encode(), salt)
_password = _password.decode('utf-8')
print(_password)
