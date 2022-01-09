from requests import get, utils

responce = utils.get_unicode_from_response(get('https://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(code):
    content = responce.split("<Valute ID=")
    for i in content:
        if code.upper() in i:
            print(code.upper(), end=" ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


print(currency_rates("uSd"))
print(currency_rates("EUR"))
