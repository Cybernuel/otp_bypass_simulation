from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"


# Login route
@app.route("/", methods=["GET", "POST"])
@app.route("/signup", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            # Generate 4-digit OTP
            otp = str(random.randint(1000, 9999))
            session["otp"] = otp
            session["username"] = username
            print(f"[DEBUG] OTP for {username} is {otp}")

            return redirect(url_for("otp"))

        return render_template("signup.html", error="Invalid details")

    return render_template("signup.html")





@app.route("/otp", methods=["GET", "POST"])
def otp():
    if "otp" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        entered_otp = request.form.get("otp")

        if entered_otp == session["otp"]:
            return "1"
        else:
            return "2"

    return render_template("otp.html")







@app.route("/success")
def success():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("success.html", username=session["username"])


if __name__ == "__main__":
    app.run(debug=True)
