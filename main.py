from flask import Flask, render_template
from dotenv import dotenv_values

app = Flask(__name__)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template("Components/home.html")
    # return render_template("home.html")

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    config = dotenv_values(".env")
    app.run(port=config["PORT"],debug=True)
    