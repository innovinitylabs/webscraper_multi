# scraper used to scrape marriage data's from tnreginet.gov.in used fro educational purposes created by @rajaspidey
import concurrent.futures
import csv
from itertools import repeat



####### SETUP #######

from /Users/shyam/Documents/Scraper2/myScraper.py import myscraper

mar_type = 'TMR1'  # 'TMR1'  'HMR'  TMR1a	SPL  SPLO CMR
#mar_year = 2015
####### SETUP #######
project_path = '/Users/shyam/Downloads/TNregi_Scrape'
logs_path = f'{project_path}logs/'

# LOAD place list from file
if mar_type == 'CMR':
    pass
    #place_list = repeat('CHURCH')
else:
    with open('placeList.txt', 'r', encoding="utf-8") as f:
        for line in csv.reader(f):
            print(' \n file reading done ! \n')
            place_list = line
            print(line)
            print('\n PLACE list successfully loaded..!! \n')

print('\n \n \n')

if __name__ == '__main__':

    # for mar_year in range (2015,2017):
    if mar_type != 'CMR':
    	for yr in (2016, 2017, 2015): #for _ in range (1,2):
    		with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
	            #year = (2015, 2016, 2017)
	            print('creating ThreadPoolExecutor')
	            start_scrape = executor.map(myscraper, repeat(mar_type), place_list, repeat(yr))#year * len(place_list))
    else:
        # myscraper(mar_type, 'CHURCH', 2015)
        # myscraper(mar_type, 'CHURCH', 2016)
        # myscraper(mar_type, 'CHURCH', 2017)

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            year = (2015, 2016, 2017)
            print('creating ThreadPoolExecutor')
            start_scrape = executor.map(myscraper, repeat(mar_type), repeat('CHURCH'), year)



        # def myscraper(mar_type, start, loc, scrape_year):
        # def check_file(mar_type, mar_place, mar_year) -> int:
        #         year = (2015, 2016, 2017)
#         start_scrape1 = executor.map(check_continuity, [i for i in p for j in year], year * len(p))
