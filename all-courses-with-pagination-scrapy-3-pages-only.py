import scrapy
from openpyxl import Workbook

class CourseTitlesSpider(scrapy.Spider):
    name = "course_titles"
    start_urls = ['https://www.oneeducation.org.uk/courses/']

    def __init__(self):
        self.workbook = Workbook()
        self.sheet = self.workbook.active

    def parse(self, response):
        # Extract course titles
        course_titles = response.css('div.course-dynamic-title a::text').getall()
        for title in course_titles:
            yield {'title': title}
            self.sheet.append([title])

        # Follow pagination links for the first 2 pages
        if response.meta.get('page') is None:
            for page in range(10):
                yield scrapy.Request(response.urljoin(f'?paged={page+1}'),
                                     meta={'page': page+1})

    def closed(self, reason):
        self.workbook.save('course_titles.xlsx')
