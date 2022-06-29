from scrape_pga import scrapePga
from send_to_db import send_to_db
import pandas as pd

drive_dist = scrapePga('https://www.pgatour.com/stats/stat.101.html')
drive_dist_df = pd.DataFrame(drive_dist)
send_to_db(drive_dist_df, 'DRIVER_DISTANCE', 'replace')

drive_acc = scrapePga('https://www.pgatour.com/stats/stat.102.html')
drive_acc_df = pd.DataFrame(drive_acc)
send_to_db(drive_acc_df, 'DRIVER_ACCURACY', 'replace')

print('Data Uploaded!')