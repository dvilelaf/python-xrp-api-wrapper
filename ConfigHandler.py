import json
import os


class ConfigHandler:

    def __init__(self, accounts: dict={},
                 server: str='wss://s.altnet.rippletest.net:51233',
                 fileName: str='.secret_config.js'):
        self.accounts = accounts
        self.server = server
        self.fileName = fileName

    @classmethod
    def fromFile(cls, fileName: str='.secret_config.js') -> 'ConfigHandler':
        if os.path.isfile(fileName):
            with open(fileName, 'r') as infile:
                data = json.loads(infile.read().replace('module.exports = ', ''))  # Beware of extra commas
                return cls(data['accounts'], data['server'], fileName)
        else:
            raise FileNotFoundError

    def save(self, fileName: str=''):
        data = {"server": self.server, "accounts": self.accounts}
        fileName = fileName if fileName else self.fileName
        with open(fileName, 'w') as outfile:
            outfile.write('module.exports = ' + json.dumps(data, indent=4))

    def __str__(self):
        data = {"server": self.server, "accounts": self.accounts}
        return f'<{self.fileName}>\nmodule.exports = ' + json.dumps(data, indent=4)

    def __repr__(self):
        return 'ConfigHandler()'
