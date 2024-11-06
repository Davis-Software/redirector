from __init__ import app

from flask import render_template, request, make_response

from utils.password_manager import auth_required
from utils.request_codes import RequestCode
from utils.valid_react_routes import VALID_REACT_ROUTES


@app.route("/admin")
@app.route("/<path:page>")
# @auth_required
def route_index(page=None):
    page_base = page.split("/")[0] if page else "/"
    not_found = page_base not in VALID_REACT_ROUTES or request.args.get("error") == RequestCode.ClientError.NotFound

    resp = make_response(
        render_template("pages/index.html"),
        RequestCode.ClientError.NotFound if not_found else RequestCode.Success.OK
    )

    return resp
