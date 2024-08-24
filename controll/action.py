import requests
from bs4 import BeautifulSoup
from data_base_query.query import q
class news:

    def start(self):
        for i in range(38,5300):
            link = "https://torob.com/browse/" + str(i)
            print(link)
            response = requests.get(link)
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')
            product_links = soup.find_all('a', href=True)
            # استخراج و چاپ لینک‌ها
            base_url = 'https://torob.com'
            for link in product_links:
                href = link['href']
                if href.startswith('/p/'):
                    full_url = base_url + href
                    if full_url == "https://torob.com/p/de0b1315-7d0a-41d4-bcf7-af1ad9ed385c/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C-redmi-note-13-4g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/":
                        break
                    else:
                        print(full_url)
                        self.add(full_url)

    def add(self,url):
        try:
            self.url = url
            self.q = q()
            self.q.connect()
            response = requests.get(self.url)
            html = response.content
            soup = BeautifulSoup(html, 'html.parser') 
            title = ""
            title = soup.find("h1",class_="jsx-e3b86428d41c997c").text.strip()
            src = ""
            image = soup.find("picture",class_="jsx-221e9d776437f763")
            mohs = image.find('img')
            src = mohs['src']
            o = ""
            text = ""
            try:
                text = soup.find("div",class_="jsx-d9bfdb7eefd5a6bf sub-section").text.strip()
                price = soup.find("div",class_="jsx-e3b86428d41c997c ellipsis")
                price_texts = price.find_all('div', class_='jsx-e3b86428d41c997c buy_box_text ellipsis')
                o1 = price_texts[1].text.strip()
                o = o1.replace("تومان","")
            except:
                pass
            catgoryy = ""
            category = soup.find("div",class_="dropdown account-dropdown")
            catgoryy = category.find("a",class_="dropdown__trigger droptrigger").text.strip()
            owner = ""
            owner1 = soup.find("div",class_="jsx-e3b86428d41c997c buy_box_text ellipsis").text.strip()
            owner = owner1.replace("خرید از ","")
            return self.q.add(title,owner,src,text,o,catgoryy,url)
        except Exception as e:
            print(f"*E*  {e}")

    def __init__(self):
        self.q = q()
        self.q.connect()