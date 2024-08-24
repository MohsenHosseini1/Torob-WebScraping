import yaml
import psycopg2
class q: 
    def __init__(self):
         with open("config_yaml\\pg.yaml") as f:
              self.config = yaml.safe_load(f)
    def connect(self): #ijad connection ba database
        self.con = psycopg2.connect(host=self.config['host'], database=self.config['database'], port=self.config['port'], user=self.config['username'], password=self.config['password'])
        self.cur = self.con.cursor()
    def add(self,title,owner,src,text,o,catgoryy,url):
        try:
            self.cur.execute(f"insert into products(owner,productname,product_description,product_price,category,image,url) values('{owner}','{title}','{text}', '{o}', '{catgoryy}', '{src}', '{url}')")
            self.con.commit()
            return False
        except Exception as e:
            print(e)
            self.con.rollback()
            return True
        