from typing import Callable
from functools import wraps

from whisper_live.client import TranscriptionClient

from .text import set_recognized_text


def _hooked_process_segments(orig_process: Callable):
    @wraps(orig_process)
    def wrapper(segments):
        for segment in segments:
            if segment["completed"]:
                text = (segment.get("text") or "").strip()
                if text:
                    set_recognized_text(text)

        return orig_process(segments)

    return wrapper


def insert_hook(client: TranscriptionClient) -> TranscriptionClient:
    client_low = getattr(client, "client", None)
    if client_low is None:
        raise RuntimeError("Не нашёл внутренний ws-клиент. "
                           "Попробуй print(dir(client)) и ищи поле с on_message/process_segments.")

    orig_process = getattr(client_low, "process_segments", None)
    if orig_process is None:
        raise RuntimeError("Не нашёл process_segments. Посмотри dir(client.client) и ищи обработчик segments.")

    client_low.process_segments = _hooked_process_segments(orig_process)

    return client
