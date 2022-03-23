from flask import Flask
app = Flask(__name__)

@app.route('/')
def first():
    return app.send_static_file("Website.html")

app.run(host = "localhost",port =5001,debug = True)
##if __name__ == "__main__":