class Compiler(object):
    def __init__(self, password):
        self.password = password
        self.characters = {'a':'hg4','b':'t9d','c':'8u3','d':'89o','e':'7fr','f':'u8e','g':'671','h':'7c5','i':'8hf','j':'hdk','k':'y8c','l':'yt7','m':'8gh','n':'84w','o':'89f','p':'23z','q':'12l','r':'vb6','s':'894','t':'8df','u':'nnm','v':'6bx','w':'8dz','x':'hid','y':'mcl','z':'irb','1':'7yg','2':'88b','3':'ewr','4':'0o0','5':'pyf','6':'824','7':'po1','8':'5t4','9':'lj1'}

    def compile(self):
        for i in self.password:
            if i in self.characters:
                compiled_password = self.password.replace(i, self.characters[i])

        return compiled password
