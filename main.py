# scraper used to scrape marriage data's from tnreginet.gov.in used for educational purposes
import concurrent.futures
import csv
from itertools import repeat
from myScraper import myscraper

####### SETUP #######

mar_type = 'TMR1'  # Options: 'TMR1'  'HMR'  'TMR1a'    'SPL'  'SPLO' 'CMR' 

####### SETUP #######
project_path = '/Users/username/Downloads/TNregi_Scrape'
logs_path = f'{project_path}logs/'

# LOAD place list from file
if mar_type == 'CMR':
    pass    
else:
    with open('placeList.txt', 'r', encoding="utf-8") as f:
        for line in csv.reader(f):
            print(' \n file reading done ! \n')
            place_list = line
            print(line)
            print('\n PLACE list successfully loaded..!! \n')

print('\n \n \n')

if __name__ == '__main__':

    if mar_type != 'CMR':

    	for yr in (2016, 2017, 2015):
            with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
                print('Creating ThreadPoolExecutor...')
                start_scrape = executor.map(myscraper, repeat(mar_type), place_list, repeat(yr))
    else:
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            year = (2015, 2016, 2017)
            print('Creating ThreadPoolExecutor...')
            start_scrape = executor.map(myscraper, repeat(mar_type), repeat('CHURCH'), year)