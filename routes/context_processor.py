from __init__ import app
from models.settings_model.settings_model import SettingsModel

from datetime import datetime


@app.context_processor
def processor():
    dictionary = dict(
        app_name=SettingsModel.get("app_name"),
        py={
            "len": len,
            "type": type,
            "zip": zip,
            "enum": enumerate,
            "round": round,
            "datetime": datetime,
            "strftime": lambda data: data.strftime("%d.%m.%Y %H:%M:%S"),
        },
    )

    return dictionary
