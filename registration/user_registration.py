import os
from credential_manager import compiler

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.usernames_file = os.path.join(self.path, '.client_usernames', 'usernames.txt')
        self.passwords_file = os.path.join(self.path, '.client_passwords', 'passwords.txt')
        self.compiler = compiler.Compiler()
        
    def register(self):
        with open(self.usernames_file) as f:
            f.write(slf.username)
            with open(self.paswords_file) as ff:
                ff.write(self.compiler(self.password).compile())
                ff.close()
            f.close()
