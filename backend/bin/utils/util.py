import os

def get_django_management_executable():
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    return execute_from_command_line

def django_management_execute(argv):
    execute_from_command_line = get_django_management_executable()
    return execute_from_command_line(argv)
