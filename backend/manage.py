#!/usr/bin/env python
import os
import sys
from contextlib import suppress

if __name__ == '__main__':
    # 初始化时创建日志目录
    with suppress(FileExistsError):
        os.makedirs('../data')
        os.makedirs('../logs')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebBugManager.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
