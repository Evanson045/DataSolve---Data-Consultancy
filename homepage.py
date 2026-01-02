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

# ✅ Feedback route removed

if __name__ == "__main__":
    # Use host=0.0.0.0 for deployment, debug=False for production
    app.run(host="0.0.0.0", port=5000, debug=False)
