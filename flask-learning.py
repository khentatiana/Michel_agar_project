from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from agarOnPython.app import db

h = generate_password_hash("foobar")

print(h)
print(check_password_hash(h, "foobar"))
print(check_password_hash(h, "lobar"))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    print(db)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


myUser = User(username='Michael', email='mbarbachov@gmail.com')
print(myUser)
myUser.set_password(input())

p = input()
while not myUser.check_password(p):
    print("Wrong Password Try Again.")
    p = input()

print('Yay you got your password correct!')
