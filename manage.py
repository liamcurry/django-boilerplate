#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    for root, dirnames, filenames in os.walk('.'):
        if 'activate_this.py' in filenames:
            path_to_activate_this = os.path.join(root, 'activate_this.py')
            execfile(path_to_activate_this,
                     dict(__file__=path_to_activate_this))
            break

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
