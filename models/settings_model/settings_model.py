from models.base_model import KeyedValueModel
from .settings_defaults import SETTINGS_DEFAULTS


class SettingsModel(KeyedValueModel):
    __tablename__ = "settings"

    @classmethod
    def ensure_defaults(cls):
        for key, value in SETTINGS_DEFAULTS.items():
            if cls.get(key) is None:
                cls(key, value).add()


# Ensure that the default settings are present in the database
SettingsModel.ensure_defaults()
