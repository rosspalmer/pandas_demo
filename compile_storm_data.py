import os
import pandas as pd
import time as tm

#|Create empty DataFrame
df = pd.DataFrame()

#|Loop through all files in 'storm_data' folder
for fn in os.listdir('./storm_data'):
	if '.csv' in fn:
		print '----Loading %s----' % fn

		#|Load individual CSV file and add to compiled DataFrame
        file_location = './storm_data/%s' % fn
        csv = pd.DataFrame.from_csv(file_location)
        df = df.append(csv, ignore_index=True)

#|Create 'compiled_data' CSV file
print '----Creating compiled CSV file----'
df.to_csv('compiled_data.csv')
print df
