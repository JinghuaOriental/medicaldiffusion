""" 定义加载yaml配置文件的函数 """
import yaml

def load_cfgs(cfg_file):
    """ load yaml config file """
    with open(cfg_file, 'r', encoding='utf-8') as f:
        cfgs = yaml.load(f, Loader=yaml.FullLoader)
    return cfgs