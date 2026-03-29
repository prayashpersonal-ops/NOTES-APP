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

if __name__ == "__main__":
    app.run(debug=True)