import os
from credential_manager import decompiler
from credential_manager import compiler

class Admin(object):
    def __init__(self, username, password):
        """Creates admin user (Generally the person who can edit everything which goes on here.)"""
        self.username = username
        self.password = password
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.usernames_file = os.path.join(self.path, '.admin_usernames', 'usernames.txt')
        self.passwords_file = os.path.join(self.path, '.admin_passwords', 'password.txt')
        self.decompiler = decompiler.Decompiler()
        self.compiler = compiler.Compiler()

    def register(self):
        with open(self.usernames_file) as f:
            lines = f.readlines()
            if len(lines) == 0:
                f.write(self.username)
                with open(self.passwords_file) as ff:
                   ff.write(self.compiler(self.password).compile())
                   ff.close()
                f.close()

            else:
                print('An admin has already been registered. Please enter his/her credentials to continue:')
                name = input('Username: ')
                try:
                    lines = f.readlines
                    if name in lines and len(name) > 0:
                        for num, line in enumerate(f, 1):
                            if self.username in line:
                                x = num
                            password = input('Password: ')
                        with open(self.passwords_file) as file:
                            lines = file.readlines()
                            pass_recieved = lines[x]
                            if password = self.decompiler(pass_recieved).decompile():
                                f.write(self.username)
                                file.write(self.compiler(self.password).compile())
                                print('Admin registered!')
                            else:
                                print('Invalid password')
                                file.close()
                    else:
                        print('No such user has registered')
                except:
                    print('An uknown error occured.')
            f.close()
                
