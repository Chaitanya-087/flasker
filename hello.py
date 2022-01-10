from flask import Flask,render_template

app = Flask(__name__)

#safe
#capitalize
#lower
#upper
#trim 
#title
#striptags

@app.route('/')
def index():
    fruits = ['mango','apple','banana','pineapple','cherry','guava']
    return render_template('index.html',fruits = fruits)

@app.route('/user')
def user():
    name = "chaitanya"
    stuff = "this is <strong>Bold</strong> text"
    return render_template('user.html',user_name = name,stuff = stuff)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)