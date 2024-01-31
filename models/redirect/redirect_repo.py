from uuid import uuid4

from .redirect_model import RedirectModel


def get_all_redirects():
    return RedirectModel.query.all()


def get_redirect_by_id(redirect_id):
    return RedirectModel.query.filter_by(id=redirect_id).first()


def get_redirect_by_slug(slug):
    return RedirectModel.query.filter_by(slug=slug).first()


def create_redirect(name, slug, url):
    if slug is None:
        slug = str(uuid4())[:8]

    try:
        redirect = RedirectModel(name, slug, url)
        redirect.add()
        return True

    except Exception as e:
        print(e)
        return False
