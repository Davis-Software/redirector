from .redirection_model import RedirectionModel
from .sub_redirection_model import SubRedirectionModel


def get_paginated_redirections(page, page_size, search=None, sort=None, asc=False):
    return RedirectionModel.query.filter(RedirectionModel.name.like(f"%{search}%") if search else True) \
        .order_by(getattr(RedirectionModel, sort) if sort else RedirectionModel.created_at) \
        .paginate(page=page, per_page=page_size)
