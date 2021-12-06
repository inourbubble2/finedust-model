import csv

gu_list = ['강남구',
           '강동구',
           '강북구',
           '강서구',
           '관악구',
           '광진구',
           '구로구',
           '금천구',
           '노원구',
           '도봉구',
           '동대문구',
           '동작구',
           '마포구',
           '서대문구',
           '서초구',
           '성동구',
           '성북구',
           '송파구',
           '양천구',
           '영등포구',
           '용산구',
           '은평구',
           '종로구',
           '중구',
           '중랑구']
dest_file = open(f'/Users/ny/Downloads/finedust_dataset/data.csv', 'w')
writer = csv.writer(dest_file)
writer.writerow(['location', 'time', 'PM10', 'SO2', 'CO', 'O3', 'NO2', 'temp', 'deg_sin', 'deg_cos', 'spd', 'rain', 'humi'])

for gu in gu_list:
    try:
        source_file = open(f'/Users/ny/Downloads/finedust_dataset/data_{gu}.csv')
    except FileNotFoundError:
        pass

    reader = csv.reader(source_file)
    lines = list(reader)[1:]

    for line in lines:
        writer.writerow([gu] + line)

    source_file.close()

dest_file.close()
