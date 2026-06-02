import configparser

class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = configparser.ConfigParser()

    def load_config(self):
        self.config.read(self.file_path)
        return self.config


class DatabaseConfig(Config):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.settings = {}

    def validate_keys(self):
        required_keys = ["host", "port", "username", "password", "dbname"]

        if "database" not in self.config:
            print("Missing [database] section")
            return False

        for key in required_keys:
            if key not in self.config["database"]:
                print("Missing key:", key)
                return False

        return True

    def get_settings(self):
        if not self.validate_keys():
            return None

        self.settings = dict(self.config["database"])
        return self.settings


config = DatabaseConfig("db.ini")
config.load_config()

settings = config.get_settings()

print("Database Settings:")
print(settings)