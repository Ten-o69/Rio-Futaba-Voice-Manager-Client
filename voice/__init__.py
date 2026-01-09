import time
import multiprocessing as mp

from whisper_live.client import TranscriptionClient

from .utils import insert_hook


def _run_client(
        host: str,
        port: int,
        lang: str,
        translate: bool,
        model: str,
        use_vad: bool,
) -> None:
    client = TranscriptionClient(
        host=host,
        port=port,
        lang=lang,
        translate=translate,
        model=model,
        use_vad=use_vad,
    )

    client = insert_hook(client)
    client()


def run_process_voice_client(
        host: str = "127.0.0.1",
        port: int = 9090,
        lang: str = "en",
        translate: bool = False,
        model: str = "small",
        use_vad: bool = False,
        wait_time: int = 3,
) -> None:
    process_client = mp.Process(
        target=_run_client,
        args=(host, port, lang, translate, model, use_vad),
        daemon=True,
    )
    process_client.start()

    time.sleep(wait_time)
    process_client.terminate()
    process_client.join()
