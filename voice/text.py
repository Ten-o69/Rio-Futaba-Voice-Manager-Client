from common.constants import DIR_TEMP, FILENAME_RECOGNIZED_TEXT


def set_recognized_text(text: str) -> None:
    with open(DIR_TEMP / FILENAME_RECOGNIZED_TEXT, "w") as f:
        f.write(text)


def get_recognized_text() -> str:
    path_recognized_text = DIR_TEMP / FILENAME_RECOGNIZED_TEXT

    if path_recognized_text.exists():
        with open(path_recognized_text, "r") as f:
            return f.read()

    else:
        return ""
