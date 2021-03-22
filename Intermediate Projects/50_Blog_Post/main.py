from flask import Flask, render_template
from post import Post
import requests

BLOG_URL = "YOUR_BLOG_URL"

posts = requests.get(BLOG_URL).json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("blog/index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("blog/post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)


