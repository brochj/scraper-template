import configparser as cfg

config = cfg.ConfigParser(interpolation=cfg.ExtendedInterpolation())
print(config.read("./configs/html_downloaders.ini"))
print(config.get("Requests", "userAgent"))
print(config["Requests"]["userAgent"])
