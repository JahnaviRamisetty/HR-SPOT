import configparser

config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class readconfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseurl')
        return url
    @staticmethod
    def getusername():
        username=config.get('common info','username')
        return username
    @staticmethod
    def getpassword():
        password= config.get('common info','password')
        return password
