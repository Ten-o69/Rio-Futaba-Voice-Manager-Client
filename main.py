from voice import run_process_voice_client
from voice.text import get_recognized_text
from settings import Settings


if __name__ == "__main__":
    run_process_voice_client(
        host=Settings.server_connection.host,
        port=Settings.server_connection.port,
        lang=Settings.server_connection.lang,
        translate=Settings.server_connection.translate,
        model=Settings.server_connection.model,
        use_vad=Settings.server_connection.use_vad,
        wait_time=Settings.client.wait_time,
    )
    print(get_recognized_text())
