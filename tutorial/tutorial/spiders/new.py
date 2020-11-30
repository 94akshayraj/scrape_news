# # coding=utf8
# import json
# from urllib.request import Request, urlopen

# headers = {'User-Agent': 'Mozilla/5.0'}
# url = "https://www.manoramaonline.com/content/mm/mo/news/just-in/_jcr_content/mm-subsection-top-left/articlelisting.results.100.100.json"
# request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
# values = {'name' : 'Michael Foord',
#           'location' : 'Northampton',
#           'language' : 'Python' }

# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
# req = urllib.request.Request(url, data, headers)
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()
# response = urlopen(request).read()
# print(response)
# # with open('news.html', 'w', encoding='utf8') as json_file:
# #     json.dump(epsg_json, json_file, ensure_ascii=False)
