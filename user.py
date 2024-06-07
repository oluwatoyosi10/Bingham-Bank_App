class user:
    def register(self, name, phone,email, password):
        return name
    def login(self, email, password):
        if email=="exam@gmail.com" and password == "123":
            return True
        else:
            return False
