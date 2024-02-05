from __init__ import config

from functools import wraps
from flask import session, request, render_template


def check_password(password) -> bool:
    return password == config.get("WEB_PASSWORD")


def check_auth():
    return session.get("logged_in")


def auth_required(func):
    @wraps(func)
    def check(*args, **kwargs):
        if not check_auth():
            return func(*args, **kwargs)
        return render_template("auth/login.html", redirect=request.path)

    return check
