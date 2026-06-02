import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def _generate_short_code(self, url):
        # Create hash and take first 6 characters
        hash_object = hashlib.md5(url.encode())
        return hash_object.hexdigest()[:6]

    def shorten_url(self, url):
        if not url:
            return "Invalid URL"

        short_code = self._generate_short_code(url)
        self.url_map[short_code] = url

        return short_code

    def get_original_url(self, short_code):
        return self.url_map.get(short_code, "URL not found")


def main():
    shortener = URLShortener()

    url = "https://www.google.com"
    short_code = shortener.shorten_url(url)

    print("Short URL code:", short_code)
    print("Original URL:", shortener.get_original_url(short_code))


main()