from flask import Flask, render_template
import requests

app = Flask(__name__)

# BLOG_URL = "https://api.npoint.io/3f470bc59dd8ae9f8edd"
BLOG_URL = "YOUR_BLOG_API_URL_HERE"

posts = requests.get(url=BLOG_URL).json()



@app.route("/")
def index():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def post(index):
    return render_template("post.html", post=posts[index-1])



if __name__ == "__main__":
    app.run(debug=True)








