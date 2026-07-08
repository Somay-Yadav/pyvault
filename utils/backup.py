import shutil
from datetime import datetime
from pathlib import Path


def create_backup():

    Path("backups").mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_name = f"backup_{timestamp}.db"

    destination = Path("backups") / backup_name

    shutil.copy2("data/vault.db", destination)

    return destination