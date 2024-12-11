class loginTools:
    def loginHandle(data, usernamekey, passwordkey):
        if data:
            username = data[0]
            password = data[1]
            
            # Memeriksa apakah username ada di usernamekey dan password sesuai dengan username tersebut
            if username in usernamekey and password == passwordkey.get(username):
                return True
            else:
                return False