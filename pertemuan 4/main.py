from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey There!'

@app.route('/aboutme')
def about_me():
    return 'Halo nama saya :<br>npm saya :<br>kelas saya :'

@app.rouet('/labti')
def labti():
    return 'Laboratorium Informatika Universitas Gunadarma'

if __name__ == '__main__':
    app.run()
