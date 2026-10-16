from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string
import os

app = Flask(__name__, static_folder="static")

BASE = os.path.dirname(os.path.abspath(__file__))

# Same credentials that are visible in the JS file
VALID_USER = "club_member"
VALID_PASS = "CyanGlow2024!"

@app.route("/")
def index():
    return send_from_directory(BASE, "index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if username == VALID_USER and password == VALID_PASS:
        return redirect(url_for("success"))

    # Failed login – show the form again with a simple error
    # (we keep it simple, no session needed)
    with open(os.path.join(BASE, "index.html")) as f:
        html = f.read()

    # Inject a visible error message
    error_html = '<p id="error" class="error" style="display:block;">Invalid credentials. Try again.</p>'
    html = html.replace(
        '<p id="error" class="error" style="display:none;"></p>',
        error_html
    )
    return html, 401

@app.route("/success")
def success():
    return send_from_directory(BASE, "success.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
