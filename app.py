from flask import Flask, render_template, redirect, request

app = Flask(__name__)

notes = []

@app.route("/")
def home():
    return render_template("index.html", notes=notes)

@app.route("/add", methods=['POST'])
def add():
    title = request.form["title"]
    textarea = request.form["textarea"]
    
    notes.append({
        "title": title,
        "textarea": textarea
    })
    
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(notes):
        notes.pop(index)
    
    return redirect("/")

import os

port = int(os.environ.get("PORT", 5000))

app.run(host="0.0.0.0", port=port)
