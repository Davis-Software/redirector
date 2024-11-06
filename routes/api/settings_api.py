from __init__ import app
from models.settings_model import SettingsModel

from flask import request


@app.route("/api/settings", methods=["GET", "POST"])
def route_get_settings():
    if request.method == "POST":
        for key, value in request.form.items():
            SettingsModel.set(key, value)
        return SettingsModel.export_to_dict()

    return SettingsModel.export_to_dict()
