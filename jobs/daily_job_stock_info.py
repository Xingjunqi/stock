import tushare as ts
import datetime
import libs.common as common

if __name__ == '__main__':
    pro=ts.pro_api('3fe9e5e0002db1ae4a43f4a7b59989ae375408a59ac7802844df2c49');

    # 接着最后一次刷新股票每日信息
    max_date_sql = "select MAX(trade_date) from ts_stock_info"
    max_date = common.select(max_date_sql)
    start = max_date[0][0]
    end = datetime.date.today().strftime('%Y%m%d')
    startdate = datetime.datetime.strptime(start, '%Y%m%d')
    enddate = datetime.datetime.strptime(end, '%Y%m%d')
    while startdate < enddate :
        startdate += datetime.timedelta(days=1)
        start = startdate.__str__().replace('-', '')[0:8]
        data = pro.daily(start_date=start, end_date=start)
        common.insert_db(data, "ts_stock_info", False, "ts_code,trade_date")
        print('daily_job_stock_info process date : %s' % (start))
        print(data)
