import os

import yaml


def _get_dir():
    return os.path.dirname(os.path.realpath('__file__'))


def read_yaml(relative_path):
    relative_path = os.path.join(_get_dir(), relative_path)
    yaml_file: dict
    with open(relative_path) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        yaml_file = yaml.load(file, Loader=yaml.FullLoader)

    return yaml_file
