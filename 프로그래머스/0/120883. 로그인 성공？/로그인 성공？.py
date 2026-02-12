def solution(id_pw, db):
    for id_pw_db in db:
        if id_pw[0] == id_pw_db[0]:
            if id_pw[1] == id_pw_db[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"