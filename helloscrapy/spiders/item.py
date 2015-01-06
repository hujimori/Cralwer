from scrapy.item import Item, Field

class FirstProjItem(Item):
	title = Field()
	link = Field()
	content = Field()