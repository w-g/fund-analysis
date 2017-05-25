import scrapy


class FundValue110020Spider(scrapy.Spider):

    name = 'fund-value-110020'

    def start_requests(self):
        return [scrapy.FormRequest('http://query2.efunds.com.cn/website/fundvalue_detail.jsp?fundcode=110020', 
                                    formdata={ 'fundValueBeginDate': '2009-05-24', 'fundValueEndDate': '2017-05-24'},
                                    callback=self.parse)]

    def parse(self, response):
        with open('./data/debug.txt', 'w') as f:
            f.write(response.body)

        for tr in response.xpath('//tr'):

            date = tr.xpath('./td[1]/div[@align="right"]/text()').extract_first()
            if date:
                date = date.strip()
                value = tr.xpath('./td[2]/div[@align="right"]/text()').extract_first().strip()
                rate = tr.xpath('./td[3]/div[@align="right"]/text()').extract_first().strip()
                value_total = tr.xpath('./td[4]/div[@align="right"]/text()').extract_first().strip()

                with open('./data/' + self.name + '.data', 'a') as f:
                    f.write(date + '#' + value + '#' + rate + '#' + value_total + '\r')