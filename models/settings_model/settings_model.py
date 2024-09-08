from models.base_model import KeyedValueModel
from models.settings_model.settings_defaults import SETTINGS


class SettingsModel(KeyedValueModel):
    __tablename__ = "settings"

    @classmethod
    def get(cls, key: str, boolean=False):
        return super().get(key, boolean) or SETTINGS.get(key)
