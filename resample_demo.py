import pandas as pd
import time as tm
from pandas.tseries.tools import to_datetime

#|Set CSV  load start time
start_csv = tm.time()

#|Load trade history CSV file
trd = pd.read_csv('btcnCNY.csv',
                  names=['timestamp','price','amount'])
print '---CSV File Loaded---'

#|Set CSV load end time
end_csv = tm.time()

#|Create datetime index from timestamp
trd['date'] = to_datetime(trd['timestamp'], unit='s')
trd = trd.set_index('date')

#|Create Series objects of 'price' and 'amount'
price = trd['price'].astype(float)
amount = trd['amount'].astype(float)

#|Set frequency of hour intervals for OLHCV conversion
freq = 'min'

#|Set resample start time
start_resample = tm.time()

#|Create index column for OLHCV price history DataFrame
prc = pd.DataFrame(index=price.resample(freq, how='last').index)

#|Resample trade history data into OLHCV price history
prc['open'] = price.resample(freq, how='first').fillna(value=0)
prc['low'] = price.resample(freq, how='min').fillna(value=0)
prc['high'] = price.resample(freq, how='max').fillna(value=0)
prc['close'] = price.resample(freq, how='last').fillna(method='ffill')
prc['volume'] = amount.resample(freq, how='sum').fillna(value=0)

#|Set resample end time
end_resample = tm.time()

#|Print results
print prc.sort(ascending=False)

print
print 'CSV Load Time: %s seconds' % str(round(end_csv-start_csv))
print
print 'OLHCV Conversion Time: %s seconds' % str(round(end_resample-start_resample))
print
