from flask import Flask, render_template, url_for

app = Flask(__name__)
class User:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def __str__(self) -> str:
        return f"First name : {self.firstname}\n Lastname : {self.lastname}"

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",title="Title passed from view to template",text="Text passed from view to template")

@app.route('/user')
def user():
    return render_template("index.html",title="Title passed from view to template",text=str(User("Adel","Iazzag")))

if __name__ == '__main__':
    app.run(debug=True)
