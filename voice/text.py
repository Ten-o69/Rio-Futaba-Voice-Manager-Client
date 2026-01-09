from common.constants import DIR_TEMP, FILENAME_RECOGNIZED_TEXT


def set_recognized_text(text: str) -> None:
    with open(DIR_TEMP / FILENAME_RECOGNIZED_TEXT, "w") as f:
        f.write(text)


def get_recognized_text() -> str:
    with open(DIR_TEMP / FILENAME_RECOGNIZED_TEXT, "r") as f:
        return f.read()
