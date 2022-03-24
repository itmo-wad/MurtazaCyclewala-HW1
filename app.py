from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/Profile')
def first():
    return render_template("Website.html")

if __name__ == "__main__":
    app.run(host = "localhost",port =5001,debug = True)