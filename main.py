from flask import Flask, render_template, request, redirect

app = Flask(__name__)

posts = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        title = request.form["title"]
        category = request.form["category"]

        posts.append({
            "title": title,
            "category": category
        })

        return redirect("/")

    return render_template("index.html", posts=posts)

@app.route("/filter/<cat>")
def filter(cat):

    filtered = [p for p in posts if p["category"] == cat]

    return render_template("index.html", posts=filtered)

if __name__ == "__main__":
    app.run(debug=True)
