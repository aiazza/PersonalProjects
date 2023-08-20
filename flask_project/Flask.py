from flask import Flask, render_template
import os

IMAGE_FOLDER = os.path.join('static', 'people_photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER


@app.route('/index')
def index():
    return 'Hello there !'


@app.route('/image')
def logo():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], '2560px-Flask_logo.svg.png')
    return render_template("index.html", user_image = full_filename)


if __name__ == "__main__":
    app.run()

