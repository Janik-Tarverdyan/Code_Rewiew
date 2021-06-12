class Language():

    allowed = ['en', 'ru', 'am']

    def get_country(self):
        import requests

        url = "https://ipinfo.io/country"
        country = requests.get(url)
        country = country.text
        country = country.split('\n')[0]

        return country.lower()
