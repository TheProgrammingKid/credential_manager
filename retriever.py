import os
import compiler

class Retriever(object):
    def __init__(self, username, password):
        """Retrieves compiled password for given username"""
        self.username = username
        self.password = password
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.usernames_file = os.path.join(self.path, '.usernames', 'usernames.txt')
        self.passwords_file = os.path.join(self.path, '.passwords', 'password.txt')

    def find_username(self):
        with open(self.usernames_file, 'r') as f:
            try:
                for num, line in enumerate(f, 1):
                    if self.username in line:
                        return num
            except Exception:
                return 'The given username is not registered'
            f.close()

    def find_password_for_username(self):
        x = self.find_username()
        file = open(self.passwords_file)
        lines = file.readlines()
        try:
            i = compiler.Compiler(self.password)
            compile_password = i.compile()
            if compile_password in lines:
                compiled_password = lines[x]
                return compiled_password
            else:
                return 'Invalid password.'

        except Exception:
            return 'Invalid password.'

    def retrieve_password(self):
        x = self.find_password_for_username()
        return x


    
