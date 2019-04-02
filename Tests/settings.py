import configparser

class ConfigSettings:
    def __init__(self, cfg_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(cfg_path)

    def getConfigSetting(self, section, key):
        try:
            ret = self.cfg.get(section,key)
        except configparser.NoOptionError:
            ret = None
        return ret
