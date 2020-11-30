# import scrapy
# import json

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"

#     def start_requests(self):
#         urls = [
#             'https://www.manoramaonline.com/news/latest-news.html'
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

    

#     def parse(self, response):
#         fullnewslist = f'fullnewslist.html'
#         parsed_list = f'parsed_list.html'
#         new = f"dddd.json"
#         ll = []
#         title_url = self.extract_title_url(response)

#         with open(fullnewslist, 'wb') as f:
#             f.write(response.body)

#             for i in title_url:
#                 print(i)
#                 # yield scrapy.Request(next_page, callback=self.parse_single_article)

#                 break
#                 # ll.append(i)
#         # a_file = open(parsed_list, "w", encoding="utf-8")
#         # json.dump(dict(ll), a_file, ensure_ascii=False).encode('utf8')

#     def parse_single_article(self, response):
#         print("2")
#         for quote in response.body:
#             print("this >>>",quote)
    
#     def extract_title_url(self, response):
#         print("3")
#         for quote in response.css('div.news-blk-001 li.articleList'):
#             title = quote.css('li.articleList a::attr(title)').get()
#             next_page = quote.css('li.articleList a::attr(href)').get()
#             # yield {
#             #     'title': quote.css('li.articleList a::attr(title)').get(),
#             #     'url': quote.css('li.articleList a::attr(href)').get(),
#             # }
#             print("4", next_page)   

#         yield scrapy.Request(next_page, callback=self.parse_single_article)

#     # def extract_single_content(self, response):
#     #     # title_url = self.extract_title_url(response)
#     #     singlenews = f'singlenews.html'
#     #     for quote in response.css('div.news-blk-001 li.articleList'):

#     #         article = quote.css('div.article rte-article p::text').get(),
#     #         print(article)

#     #         with open(singlenews, 'wb') as f:
#     #             f.write(response.body)

        # file = open(fullnewslist, 'r', encoding="utf8").read()
        # self.parse_json(file)

        # if response.css('div.news-blk-001 li.articleList'):
        #     with open(fullnewslist, 'wb') as f:
        #         f.write(response.body)
        #     print("IN IF >>")
        #     for quote in response.css('div.news-blk-001 li.articleList'):
        #         title = quote.css('li.articleList a::attr(title)').get()
        #         next_page = quote.css('li.articleList a::attr(href)').get()
        #         print("next_page",next_page)
        #         if next_page in np_list:
        #             pass
        #         else:
        #             np_list.append(next_page)
        #         if next_page is not None:
        #             print("loading_next_page >")
        #             yield response.follow(next_page, self.parse)
        # else:
        #     print("IN ELSE >>")
        #     singlenews = f"singlenews.html"
        #     article = f"article.txt"
        #     dd = {}
        #     for quote in response.css('div.story-header'):
        #         title = quote.css('h1.story-headline::text').get()
        #     for quote in response.css('div.rte-article'):
        #         print("IN ELSE QUOTE >>")

        #         para = quote.css('p::text').get()
        #         dd[title] = para
        #         print("para >> ",dd)
   
        #         with open('article.json', 'a', encoding='utf-8') as f:
        #             json.dump(dd, f, ensure_ascii=False, indent=4)
        #     yield scrapy.Request(url='https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.100.100.json', callback=self.parse)

                
        #         # break
    # def clean_unsupported_chars(line, extra_chars):
    #     remove_re = compile(u'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F%s]'
    #                         % extra_chars)
    #     new_line = remove_re.subn('', line)
    #     return new_line

    # with open(article, 'w', encoding="utf-8") as f:
    #     f.write(para)
    # def extract_single_content(self, response):
    #     # title_url = self.extract_title_url(response)
    #     singlenews = f'singlenews.html'
    #     for quote in response.css('div.news-blk-001 li.articleList'):

    #         article = quote.css('div.article rte-article p::text').get(),
    #         print(article)

    #         with open(singlenews, 'wb') as f:
    #             f.write(response.body)
