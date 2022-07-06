import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.0.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.2500.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.5000.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.7500.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.10000.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.12500.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.15000.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.17500.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.20000.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.22500.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.25000.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.27500.2500.json',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.write_url_to_file)

    def write_url_to_file(self, response):
        fullnewslist = f'fullnewslist.txt'
        with open(fullnewslist, 'wb') as f:
            f.write(response.body)
        return self.get_single_news_body()
    
    def get_single_news_body(self):
        fullnewslist = f'fullnewslist.txt'
        with open(fullnewslist, 'r', encoding="utf-8") as f:
            f = f.read()
            f = f.replace("'", '"')
            jj = json.loads(f)
            urls_list =[]
            for i in json.loads(jj['articleList']):
                urls_list.append(i['url'])
            for url in urls_list:
                yield scrapy.Request(url=url, callback=self.save_fetched_json)
    def save_fetched_json(self, response):

        resp = self.parse_html_from_url(response)
        c = 0        
        
        for i in resp:
            with open('article.json', 'a', encoding='utf-8') as f:
                c = c+1
                # print("Dumped ", c, " docs")
                json.dump(i, f, ensure_ascii=False, indent=4)
        
    def parse_html_from_url(self, response):
        headline = ""
        para = ""
        for story in response.css('div.story-header'):
            headline = story.css('h1.story-headline::text').get(),
        for article in response.css('div.rte-article'):
            para = article.css('p::text').get(),
        yield {
            'headline' : headline[0],
            'para': para[0]
            }