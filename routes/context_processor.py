from __init__ import app, config

from datetime import datetime


@app.context_processor
def processor():
    dictionary = dict(
        py={
            "len": len,
            "type": type,
            "zip": zip,
            "enum": enumerate,
            "round": round,
            "datetime": datetime,
            "strftime": lambda data: data.strftime("%d.%m.%Y %H:%M:%S"),
        },
        app_name=config.get("NAME", "Unnamed")
    )

    return dictionary
