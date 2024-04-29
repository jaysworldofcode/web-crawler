# this interface is use for other libraries when scraping data
class IUrlParser:
    def parse(self, url):
        pass
    def getLinks(self) -> list[str]:
        pass