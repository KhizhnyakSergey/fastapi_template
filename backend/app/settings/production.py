from pydantic import BaseSettings


class Setting(BaseSettings):

    class Config:
        env_file = '.envs/production'