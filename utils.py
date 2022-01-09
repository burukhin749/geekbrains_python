from datetime import datetime
from requests import get, utils

responce = utils.get_unicode_from_response(get('https://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(code):
    content = responce.split("<Valute ID=")

    for i in content:
        if code.upper() in i:
            print(datetime.strptime(content[0].split('"')[-4], '%d.%m.%Y').date(), ", ", sep="", end="")
            print(code.upper(), end=", ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


if __name__ == "__main__":
    word = argv[1]
    print(currency_rates(word))
