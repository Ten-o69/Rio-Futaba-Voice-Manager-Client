import yaml
import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from common.constants import (
    DIR_BASE,
    FILENAME_SETTINGS
)
from .models import Settings


def _transformation_settings_models(
        settings_models: dict[str, type[BaseModel]],
        settings_models_kwargs: dict[str, dict[str, Any]] | None = None
) -> dict[str, type[BaseModel]]:
    transformed_models = {}

    if settings_models_kwargs is None:
        transformed_model = lambda key_, model_: model()

    else:
        transformed_model = lambda key_, model_: model(**settings_models_kwargs.get(key_, {}))

    for key, model in settings_models.items():
        transformed_models[key] = transformed_model(key, model)

    return transformed_models


def _create_settings_file(
        path_settings: Path,
        settings_models: dict[str, type[BaseModel]],
) -> None:
    path_settings.touch()
    default_settings = _transformation_settings_models(settings_models)
    default_settings = json.loads(Settings(**default_settings).model_dump_json())

    with open(path_settings, "w") as f:
        yaml.dump(default_settings, f)


def get_settings(settings_models: dict[str, type[BaseModel]]) -> Settings:
    path_settings = DIR_BASE / FILENAME_SETTINGS

    if not path_settings.exists():
        _create_settings_file(path_settings, settings_models)

    with open(DIR_BASE / FILENAME_SETTINGS, 'r') as f:
        settings: dict = yaml.safe_load(f)

        settings_models_kwargs = {}
        for setting_key in settings.keys():
            model = settings_models.get(setting_key, None)

            if model is not None:
                settings_models_kwargs[setting_key] = settings[setting_key]

        settings = _transformation_settings_models(settings_models, settings_models_kwargs)
        return Settings(**settings)
