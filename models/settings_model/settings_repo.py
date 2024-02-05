from models.settings_model.settings_model import SettingsModel
from models.settings_model.settings_defaults import SETTINGS


def ensure_defaults():
    for key, value in SETTINGS.items():
        if not SettingsModel.get(key):
            SettingsModel(key, value)

