import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/promt.py",
    ".env",
    "setup.py",
    "research/trails.ipynb",
    "app.py",
    "store_index.py",
    "static",  # This should be treated as a directory
    "templates/chat.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    # Check if the filepath is a directory
    if filepath.suffix == "":
        os.makedirs(filepath, exist_ok=True)
        logging.info(f"Creating directory: {filepath}")
    else:
        filedir, filename = os.path.split(filepath)
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file {filename}")

        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, 'w') as f:
                pass
            logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"{filename} already exists")
