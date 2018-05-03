from sendmail import sendmail
from weatherjson import get_weather
def list():
    return ['1756384121@qq.com']
def main():
    sendmail(get_weather(),list())

if __name__ == '__main__':
    main()
