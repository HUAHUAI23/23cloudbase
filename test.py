from flask import Flask

app = Flask(__name__)

def home():
    return 'Home Page'

def user_profile(username):
    return f'User: {username}'

app.add_url_rule('/', 'home', home)
app.add_url_rule('/user/<username>', 'user_profile', user_profile)

if __name__ == '__main__':
    app.run()
