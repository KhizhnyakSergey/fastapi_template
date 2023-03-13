from pydantic import BaseSettings


class Setting(BaseSettings):
    pg_echo: bool = True

    class Config:
        env_file = '.envs/development'