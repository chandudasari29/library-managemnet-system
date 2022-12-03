from csv import DictReader

from flask import Flask,request
from flask import render_template
app = Flask(__name__)
with open("BOOKS.csv", 'r') as f:
    dict_reader = DictReader(f)

    bookslist = list(dict_reader)

@app.route("/", methods=["GET","POST"])
def mainindex ():
    if request.method=="GET":
        return render_template("HOME.html.jinja2", bookslist=bookslist)
    elif request.method=="POST":
        type = request.form["type"]
        filtervalue = request.form["filtervalue"]
        return render_template("HOME2.html.jinja2",type=type, filtervalue=filtervalue ,bookslist=bookslist)
    else:
        print("Error")

if __name__ == '__main__':
    app.debug=True
    app.run()