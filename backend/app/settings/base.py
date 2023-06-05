from pydantic import BaseSettings, PostgresDsn
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(raise_error_if_not_found=True))


class Setting(BaseSettings):
    pg_dsn: PostgresDsn
    pg_echo: bool = False
    pg_future: bool = True
    access_token_expires_in: int 
    refresh_token_expires_in: int
    jwt_algorithm: str
    jwt_private_key: str
    jwt_public_key: str
    client_origin: str
    email_sender: str
    email_password: str


    def __init__(self, module: BaseSettings = None, *args, **kwargs) -> None:
        super(Setting, self).__init__(*args, **kwargs)

        if module:
            self.__dict__.update(**module().__dict__)
