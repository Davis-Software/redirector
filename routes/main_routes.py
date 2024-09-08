from __init__ import app

from flask import render_template


@app.route("/admin")
def route_index():
    return render_template("pages/index.html")
