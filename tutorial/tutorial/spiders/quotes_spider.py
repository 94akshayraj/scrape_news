import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            # 'https://www.manoramaonline.com/content/mm/mo/news/only-in-manorama-online/_jcr_content/mm-subsection-top-left/indepthinside.results.15.90.json'
            # 'https://www.manoramaonline.com/content/mm/mo/news/only-in-manorama-online/_jcr_content/mm-subsection-top-right/articlelisting.results.0.2500.json',
            # 'https://www.manoramaonline.com/content/mm/mo/news/india/_jcr_content/mm-subsection-top-left/articlelisting.results.30.5.json'
            # 'https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.30.10.json'
            # 'https://www.manoramaonline.com/content/mm/mo/news/world/_jcr_content/mm-subsection-top-left/articlelisting.results.35.5.json'
            # 'https://www.manoramaonline.com/content/mm/mo/movies/movie-news/_jcr_content/mm-subsection-top-left/articlelisting.results.30.5.json'
            # 'https://www.manoramaonline.com/content/mm/mo/health/health-news/_jcr_content/mm-subsection-top-left/articlelisting.results.25.5.json'
            # 'https://www.manoramaonline.com/content/mm/mo/health/well-being/_jcr_content/mm-subsection-top-left/articlelisting.results.25.5.json'
            # 'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.21.6.json'
            # ==
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.0.2500.json',
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.2500.2500.json',
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.5000.2500.json',
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.7500.2500.json',
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.10000.2500.json',
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.12500.2500.json',
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.15000.2500.json',
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.17500.2500.json',
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.20000.2500.json',
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.22500.2500.json',
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.25000.2500.json',
            'https://www.manoramaonline.com/content/mm/mo/fasttrack/_jcr_content/mm-section-top-left/channelallstories.results.27500.2500.json',
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
            urls_list =[]
            try:
                jj = json.loads(f)
                for i in json.loads(jj['articleList']):
                    urls_list.append(i['url'])
            except json.decoder.JSONDecodeError:
                pass
            
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