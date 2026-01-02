from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-in-prod")

# --- Mail configuration ---
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME") or "datasolveke@gmail.com"
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")  # Gmail App Password
app.config["MAIL_DEFAULT_SENDER"] = app.config["MAIL_USERNAME"]  # ✅ Default sender

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html", current_page="home")

@app.route("/services")
def services():
    return render_template("services.html", current_page="services")

@app.route("/contact")
def contact():
    return render_template("contact.html", current_page="contact")

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        user_name = request.form.get("name")
        user_feedback = request.form.get("feedback")

        msg = Message(
            subject=f"New Feedback from {user_name}",
            recipients=["datasolveke@gmail.com"]  # sender auto‑set from MAIL_DEFAULT_SENDER
        )
        msg.body = f"""
        You have new feedback:

        Name: {user_name}
        Feedback: {user_feedback}
        """

        try:
            mail.send(msg)
            flash("✅ Feedback sent successfully!", "success")
        except Exception as e:
            flash(f"❌ Error sending feedback: {e}", "danger")

        return redirect(url_for("feedback"))

    return render_template("feedback.html", current_page="feedback")

if __name__ == "__main__":
    # Debugging: confirm mail config values before running
    print("MAIL_USERNAME:", app.config["MAIL_USERNAME"])
    print("MAIL_DEFAULT_SENDER:", app.config["MAIL_DEFAULT_SENDER"])
    app.run(host="0.0.0.0", port=5000, debug=True)
