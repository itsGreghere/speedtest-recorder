import speedtest
import datetime
import csv
import time

s = speedtest.Speedtest()

file_name = 'speedtest_data.csv'

# TODO - if file not there, create and write header

while True:
    with open(file_name, 'a', newline='') as speedcsv:
        csv_writer = csv.writer(speedcsv)
        # csv_writer.writeheader()

        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
        csv_writer.writerow([
            str(time_now),
            str(downspeed),
            str(upspeed)
        ])
        # seconds to sleep between tests
        time.sleep(300)
