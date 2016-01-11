from  flask import Flask, render_template, url_for, request, redirect
from flask_wtf import Form

app = Flask(__name__)

@app.route("/")
def main():
  return render_template("main.html")

@app.route('/', methods=['POST'])
def entry():
  hashes = list()
  userquery = request.form['user-query']
  if " " in userquery:
    hashes = userquery.split(" ") 

  if request.method == 'POST':
    return redirect(url_for('index'))

@app.route("/index")
def index():
  return render_template("index.html") 

if __name__ == "__main__":
  app.run()
