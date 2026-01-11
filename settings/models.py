from pydantic import BaseModel


class ServerConnectionSettings(BaseModel):
    host: str = "127.0.0.1"
    port: int = 9090
    lang: str = "en"
    translate: bool = False
    model: str = "small"
    use_vad: bool = False


class ClientSettings(BaseModel):
    wait_time: int = 15


class Settings(BaseModel):
    server_connection: ServerConnectionSettings
    client: ClientSettings

SETTINGS_MODELS = {
    "server_connection": ServerConnectionSettings,
    "client": ClientSettings,
}
