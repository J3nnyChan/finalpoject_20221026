from datetime import date
from datetime import datetime
import sqlalchemy as db
import pymysql
from sqlalchemy import create_engine
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, session
from flask_moment import Moment
import math
from sqlalchemy import func
from collections import Counter

app = Flask(__name__)

#連接資料庫
username = 'jenny'     # 資料庫帳號
password = '123456'     # 資料庫密碼
host = '172.22.35.211'    # 資料庫位址
port = '3306'         # 資料庫埠號
database = 'news'   # 資料庫名稱
table = 'news1'   # 表格名稱

# 建立資料庫引擎
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
# 建立資料庫連線
connection  = engine.connect()



@app.route('/data-list')
def data_list():

    sql='SELECT date, label, title, content, url FROM news.news1;'
    df = pd.read_sql_query(sql, engine, coerce_float=True)

    

    # query string/page=1
    page = int(request.args.get('page',1) )
    per_page = int(request.args.get('per_page',10))

    
    connection  = engine.connect()


    total_pages = Counter(df)
    
  

    # set total pages
    total_pages = math.ceil(len(df)/per_page)
    
    



    # Close connection
    connection.close()
    
    return render_template('data_list.html',
                           page_header="幣圈新聞",
                           total_pages=total_pages,
                           outputs=df, 
                           page=page)



if __name__ == "__main__":
    app.run(debug=True)




# -----------UPDATE addressLine2 and restore database--------------
# query = db.update(table_office).where(table_office.c.officeCode == "5").values(addressLine2=None)
# proxy = connection.execute(query)
# from sqlalchemy import Integer
# query = db.delete(table_office).where(table_office.c.officeCode.cast(Integer) >7)
# proxy = connection.execute(query)
# -----------UPDATE addressLine2 and restore database--------------

