from flask import Flask, render_template, request

app = Flask(__name__)

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
        # For now, just print feedback to console (later save to DB/file)
        print(f"Feedback from {user_name}: {user_feedback}")
        return render_template("feedback.html", current_page="feedback", success=True)
    return render_template("feedback.html", current_page="feedback")

if __name__ == "__main__":
    # Use host=0.0.0.0 for deployment, debug=False for production
    app.run(host="0.0.0.0", port=5000, debug=False)
