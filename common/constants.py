from pathlib import Path
import tempfile

# dir
DIR_BASE = Path(__file__).parent.parent
DIR_TEMP = Path(tempfile.mkdtemp(prefix="rfvm_"))

# filename
FILENAME_RECOGNIZED_TEXT = "recognized_text.txt"
FILENAME_SETTINGS = "settings.yml"
