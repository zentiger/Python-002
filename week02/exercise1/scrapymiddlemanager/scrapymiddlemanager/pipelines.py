# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

DbInfo = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'geektime',
    'db': 'quotes'
}
'''
quotes的建表语句
CREATE TABLE `quotes` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `author` varchar(50) NOT NULL DEFAULT '',
  `quotes` varchar(1024) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4
'''

class DBConn(object):
    def __init__(self, DbInfo):
        self.host = DbInfo['host']
        self.port = DbInfo['port']
        self.user = DbInfo['user']
        self.password = DbInfo['password']
        self.db = DbInfo['db']
        self.conn = pymysql.connect(host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
            )

    def exec(self, sql):
        cur  = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        cur.close()

    def __del__(self):
        self.conn.close()

class QuotesPipeline:
    def __init__(self):
        self.db = DBConn(DbInfo)

    def process_item(self, item, spider):
        insert_sql = f"insert into quotes (id,author,quotes) VALUES(NULL,\"{item['author']}\",\"{item['quotes']}\")"
        self.db.exec(insert_sql)
        return item
