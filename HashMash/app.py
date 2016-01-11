from  flask import Flask, render_template, url_for, request
from flask_wtf import Form

app = Flask(__name__)

@app.route("/")
def main():
  return render_template("index.html")

@app.route("/index")
def index():
  return render_template("index.html")

if __name__ == "__main__":
  app.run()
