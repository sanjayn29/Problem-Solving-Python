class Codec:
    url = {}
    idd = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.idd += 1
        key = str(self.idd)
        self.url[key]=longUrl
        return "https://sanjayn.me/"+key
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.split("/")[-1]
        return self.url[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))