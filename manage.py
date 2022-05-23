#!/usr/bin/env python
import os
import sys




if __name__ == "__main__":
    
    sys.argv[0] = "/home/vo0/Projects/sites-voo/manage.py"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
