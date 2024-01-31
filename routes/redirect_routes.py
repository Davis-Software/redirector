from __init__ import app

from models.redirect import redirect_repo
from utils.password_manager import auth_required

from flask import request, render_template, redirect, flash, make_response


@app.route("/admin")
@auth_required
def route_list():
    return render_template(
        "pages/list.html",
        redirections=redirect_repo.get_all_redirects()
    )


def redirect_post(req, action, mode):
    name = req.form.get("name", "").strip()
    slug = req.form.get("slug", "").strip()
    url = req.form.get("url", "").strip()

    if name == "" or url == "":
        return render_template(
            "pages/edit.html",
            mode=mode,
            redirection={
                "name": name,
                "slug": slug,
                "url": url
            },
            alert={
                "type": "danger",
                "message": "Failed to create redirection. Make sure all required fields are filled out."
            }
        )

    resp = action(name, slug if slug != "" else None, url)

    return redirect("/admin") if resp else render_template(
        "pages/edit.html",
        mode=mode,
        redirection={
            "name": name,
            "slug": slug,
            "url": url
        },
        alert={
            "type": "danger",
            "message": "Failed to create redirection. Does the slug already exist?"
        }
    )


@app.route("/new", methods=["GET", "POST"])
@auth_required
def route_new():
    if request.method == "GET":
        return render_template(
            "pages/edit.html",
            redirection=None,
            mode="new",
            alert={
                "type": "info",
                "message": "Create a new redirection by filling out the form below."
            }
        )
    elif request.method == "POST":
        flash("Redirect created successfully.", "success")
        return redirect_post(request, redirect_repo.create_redirect, "new")


@app.route("/<action>/<redirect_id>", methods=["GET", "POST"])
@auth_required
def route_redirect_action(action, redirect_id):
    redirect_obj = redirect_repo.get_redirect_by_id(redirect_id)
    if redirect_obj is None:
        flash("Redirect not found.", "danger")
        return redirect("/")

    if action == "info":
        return render_template(
            "pages/info.html",
            redirection=redirect_obj
        )

    elif action == "edit":
        if request.method == "GET":
            return render_template(
                "pages/edit.html",
                redirection=redirect_obj,
                mode="edit",
                alert={
                    "type": "info",
                    "message": "Edit the redirection below."
                }
            )
        elif request.method == "POST":
            def edit(name, slug, url):
                redirect_obj.edit(name, slug, url)
                return True
            flash("Redirect edited successfully.", "success")
            return redirect_post(request, edit, "edit")

    elif action == "activate":
        redirect_obj.edit(active=True)
        flash("Redirect activated successfully.", "success")
        return redirect("/")

    elif action == "deactivate":
        redirect_obj.edit(active=False)
        flash("Redirect deactivated successfully.", "success")
        return redirect("/")

    elif action == "delete":
        redirect_obj.delete()
        flash("Redirect deleted successfully.", "success")
        return redirect("/")

    return redirect("/")


@app.route("/<slug>")
def route_redirect(slug):
    redirect_obj = redirect_repo.get_redirect_by_slug(slug)
    if redirect_obj is None or not redirect_obj.active:
        return make_response("Redirect not found.", 404)

    redirect_obj.download_request(
        # request.remote_addr,
        request.headers.get("X-Forwarded-For") or request.headers.get("Forwarded") or
        (request.remote_addr if not request.remote_addr.startswith("127.") else "unknown"),
        request.headers.get("User-Agent"),
        request.referrer or "",
        ",".join([f"{k}={v}" for k, v in request.args.items()]) or ""
    )

    return redirect(redirect_obj.url)
