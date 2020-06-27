import datetime
import logging
from backtrader.feeds import YahooFinanceData
from dateutil.relativedelta import relativedelta


logger = logging.getLogger(__name__)

def get_data(dataname,period,last_years=10):

    todate = datetime.datetime.now()

    fromdate =  (todate - relativedelta(years=last_years))

    logger.info(f"Getting {dataname} in {period} timeframe from {fromdate.strftime('%Y-%m-%d %H:%M:%S')} to {todate.strftime('%Y-%m-%d %H:%M:%S')}")

    # Create a Data Feed
    data = YahooFinanceData(
        dataname=dataname,
        period=period,
        # Do not pass values before this date
        fromdate=fromdate,
        # Do not pass values after this date
        todate=todate,
        reverse=False)

    
    return data