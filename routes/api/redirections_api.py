from __init__ import app
from models.redirection_request_model import RedirectionRequestModel
from models.redirection_model import RedirectionModel, SubRedirectionModel, get_paginated_redirections

from flask import request


@app.route("/api/redirections", methods=["GET"])
def route_get_redirections():
    search = request.args.get("search", None, type=str)
    sort = request.args.get("sort", "created_at", type=str)
    asc = request.args.get("asc") == "true"

    page = request.args.get("page", 1, type=int)
    page_size = request.args.get("page_size", 25, type=int)

    paginated_redirections = get_paginated_redirections(page, page_size, search, sort, asc)
    return [redirection.to_dict() for redirection in paginated_redirections.items]

