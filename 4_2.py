from requests import get, utils
responce = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))
content = responce.split("<Valute ID=")
for i in content:
    if "uSd".upper() in i:
        print("uSd".upper(), end=" ")
        print(i.replace("/", "").split("<Value>")[-2].replace(",", "."))
