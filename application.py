from flask import Flask, render_template, request

app = Flask(__name__)

notes = []


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
        delete=request.form.get("delete")
        if delete:
            delete=int(delete)
            del notes[delete-1]
        else:
            pass
    return render_template("index.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
