import requests
from bs4 import BeautifulSoup
import datetime
from mail import send_mail


class dm():
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        self.base_url = 'http://www.yxdm.tv'
              
    # 获取今天更新的动画的名称和网址
    def get_dm_lists(self):
        dm_dict = {}

        for i in range(1, 4):
            url = 'http://www.yxdm.tv/resource/15-{}.html'.format(i)
            r = requests.get(url, headers=self.headers)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'lxml')
            all_list = soup.find('div', class_='dhnew search-cnt adj').find_all('li')

            for li in all_list:
                url = self.base_url + li.find('p').find('a')['href']
                name = li.find('p').find('a')['title']
                time = li.find_all('p')[-2].get_text().replace('更新:', '')
                yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%m-%d")
                if time == yesterday:
                    dm_dict[name] = url
        return dm_dict

    #   过滤
    def filter_url(self, url_dict):
        necessary = ['食戟之灵第三季', '咕噜咕噜魔法阵第三季']
        dm_dict = {}
        for i in necessary:
            if i in url_dict:
                dm_dict[i] = url_dict[i]
        return dm_dict

    def get_detail(self, dm_lists):
        for name, url in dm_lists.items():
            try:
                r = requests.get(url, headers=self.headers)
                r.encoding = r.apparent_encoding
                soup = BeautifulSoup(r.text, 'lxml')

                series = soup.find('div', class_='down-content xzdis')
                series_name = series.find('a').get_text()
                pan_url = self._get_pan_url(series.find('a')['href'])  # 获得网盘链接
                pan_password = pan_url.split('@@')[-1]
                # time = soup.find('ul', class_='info1-left').find_all('li')[-1].find('p').get_text().strip()
                if len(pan_password) != 4:
                    password = ''
            except AttributeError:
                name, series_name, pan_url, pan_password = None, None, None, None

            yield name, series_name, pan_url, pan_password

    def _get_pan_url(self, url):
        r = requests.get(url, headers=self.headers)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'lxml')
        url = soup.find('div', id="down").find('a')['href']
        return url

    @property
    def addresses(self):
        import os 
        path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path,'user.txt'), 'r') as f:
            return f.readlines()[0]
