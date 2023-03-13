import os

from dotenv import load_dotenv, find_dotenv

from .base import Setting

load_dotenv(find_dotenv(raise_error_if_not_found=True))
module = os.getenv('SETTINGS_MODULE')


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