import scrapy


class PanchangSpider(scrapy.Spider):
    name = "panchang"
    start_urls = [
        "https://www.drikpanchang.com/astrology/prediction/dhanu-rashi/dhanu-rashi-daily-rashiphal.html"
    ]

    def parse(self, response, **kwargs):
        title = response.css("title::text").get()
        daily_prediction = (
            response.xpath(
                "//div[contains(@class,'dpMainPredictionCard')]/child::*/*"
            )
            .xpath("descendant::*[contains(@class, 'dpContent')]//text()")
            .extract_first()
        )

        yield {"title": title, "prediction": daily_prediction}
