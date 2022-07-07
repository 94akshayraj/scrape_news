import scrapy
import json
from datetime import timedelta, datetime


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = []
        global base_url
        base_url = 'https://malayalam.oneindia.com'
        date = datetime.strptime('2020/05/01', '%Y/%m/%d').date()
        # print(date, type(date), date.strftime('%d/%m/%Y'), type(str(date)))

        while date != datetime.strptime('2022/04/20', '%Y/%m/%d').date():
            date += timedelta(days=1)
            url = base_url + "/" + str(date.strftime('%Y/%m/%d')) + "/"
            urls.append(url)
        for url in urls:
            try:
                yield scrapy.Request(url=url, callback=self.write_url_to_file)
            except:
                pass
    def write_url_to_file(self, response):
        for story in response.css('div.dayIndexContent'):
            headline = story.css('a::attr(href)').get(),
            try:
                url = base_url+headline[0]
                yield scrapy.Request(url=url, callback=self.save_fetched_json)
            except:
                pass

    def get_single_news_body(self, response):
        story = ""
        for headline in response.css('h1.heading::text'):
            headline = headline.get()
        for sent in response.css('div.oi-article-lt p::text')[:2]:
            story = story + " " + sent.get()
        yield {
            'headline': headline,
            'para': story
        }

    def save_fetched_json(self, response):

        resp = self.get_single_news_body(response)
        c = 0

        for i in resp:
            with open('article.json', 'a', encoding='utf-8') as f:
                c = c+1
                # print("Dumped ", c, " docs")
                json.dump(i, f, ensure_ascii=False, indent=None)
