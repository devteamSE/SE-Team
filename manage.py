#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Add the app python lib to sys path
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    p_dir = os.path.normpath(os.path.join(curr_dir, '../'))
    lib_dir = os.path.normpath(os.path.join(p_dir, 'lib/python2.7/'))
    sys.path.insert(0, lib_dir)
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
