import os
from pathlib import Path
from typing import Any

from .base import Setting


module = os.getenv('SETTINGS_MODULE')
ROOT_DIR = Path(__file__).resolve().parent.parent

def path(*paths: tuple[Any], base_path: Path | str = ROOT_DIR) -> str:
    
    resolved = []
    for path in paths:
        if isinstance(path, str):
            resolved.append(path)
        else:
            resolved.extend(path)

    return os.path.join(base_path, *resolved)

match module:
    case 'development':
        from .development import Setting as AdditionalSetting
    case 'production':
        from .production import Setting as AdditionalSetting
    case 'test':
        from .test import Setting as AdditionalSetting
    case _:
        raise TypeError('SETTINGS_MODULE is required')
    
settings = Setting(_env_file=AdditionalSetting.Config.env_file, module=AdditionalSetting)


