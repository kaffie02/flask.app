from flask import request

class getDataLogin:
    def putData(slot_a, slot_b):
        if(request.method == 'POST'):
            username = request.form.get(slot_a)
            password = request.form.get(slot_b)
            return (username, password)
        return  None