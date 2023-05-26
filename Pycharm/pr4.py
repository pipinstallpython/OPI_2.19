#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
from datetime import datetime

# Найти последний измененный файл
if __name__ == "__main__":
    time, file_path = max((f.stat().st_mtime, f)
                          for f in pathlib.Path.cwd().iterdir())
    print(datetime.fromtimestamp(time), file_path)
