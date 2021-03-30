from flask import Flask, render_template, request
import requests
import smtplib


app = Flask(__name__)

# BLOG_URL = "https://api.npoint.io/3f470bc59dd8ae9f8edd"
BLOG_URL = "YOUR_BLOG_API_URL_HERE"
MAIL="YOUR_EMAIL_ADDRESS"
MAIL_PASSWORD = "YOUR_EMAIL_PASSWORD"
    
posts = requests.get(url=BLOG_URL).json()


def send_mail(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\n" \
                    f"Phone No: {phone}\nMessage:{message}"

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MAIL, password=MAIL_PASSWORD)
        connection.sendmail(from_addr=MAIL, to_addrs=MAIL,
                            msg=email_message)


@app.route("/")
def index():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':  # get data from the form
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_mail(name, email, phone, message) # send the mail

        return render_template("contact.html", response=True)

    return render_template("contact.html", response=False)

@app.route("/post/<int:index>")
def post(index):
    return render_template("post.html", post=posts[index-1])



if __name__ == "__main__":
    app.run(debug=True)








