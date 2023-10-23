import os.path
import yaml


# 获取项目的根路径
def get_root_path():
    return os.path.dirname(__file__).split('common')[0]


def read_yaml(yamlpath):
    with open(get_root_path() + yamlpath, "r", encoding="utf-8") as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value


if __name__ == '__main__':
    print()
