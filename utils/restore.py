import shutil
from pathlib import Path


BACKUP_DIR = Path("backups")
DATABASE = Path("data/vault.db")


def list_backups():
    """Return all available backup files."""

    BACKUP_DIR.mkdir(exist_ok=True)

    backups = sorted(
        BACKUP_DIR.glob("*.db"),
        reverse=True,
    )

    return backups


def restore_backup(backup_path):
    """Restore the selected backup."""

    shutil.copy2(
        backup_path,
        DATABASE,
    )