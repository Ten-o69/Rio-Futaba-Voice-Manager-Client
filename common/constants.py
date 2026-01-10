from pathlib import Path
import tempfile

from settings.models import (
    ServerConnectionSettings,
    ClientSettings
)

# dir
DIR_BASE = Path(__file__).parent.parent
DIR_TEMP = Path(tempfile.mkdtemp(prefix="rfvm_"))

# filename
FILENAME_RECOGNIZED_TEXT = "recognized_text.txt"
FILENAME_SETTINGS = "settings.yml"

# settings
SETTINGS_MODELS = {
    "server_connection": ServerConnectionSettings,
    "client": ClientSettings,
}
