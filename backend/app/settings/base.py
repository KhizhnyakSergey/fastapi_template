from pydantic import BaseSettings, PostgresDsn


class Setting(BaseSettings):
    pg_dsn: PostgresDsn
    pg_echo: bool = False
    pg_future: bool = True

    def __init__(self, module: BaseSettings = None, *args, **kwargs) -> None:
        super(Setting, self).__init__(*args, **kwargs)

        if module:
            self.__dict__.update(**module().__dict__)
