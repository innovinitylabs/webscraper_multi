# for fetching missing data which gets details of missing data from the file created by check_reg_continuity.py
import re
import concurrent.futures
from itertools import repeat

from myMissedScraper import my_missed_scraper

project_path = 'C:\\Users\\username\\PycharmProjects\\TNregi_Scrape\\'
logs_path = f'{project_path}logs\\'
missed_data = []

def fetch_missing_data() -> tuple[list[int], list, list]:
    missed_reg_no = []
    missed_place_name = []
    missed_mar_year = []

    file_path = (f'{project_path}Combined missing.txt')

    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        print(f'lines -----> {lines}')

        for line in lines:
            reg_no = int(re.findall("(?<=/)\\d+(?=/\\d+)", line)[0]) - 1
            place_name = re.findall("(?<=\[')[A-Za-z0-9 \-()_.]+(?=/\\d+/\\d+'])", line)[0]
            mar_year = re.findall("(?<=\\d/)\\d+(?=')", line)[0]
            missed_reg_no.append(reg_no)
            missed_place_name.append(place_name)
            missed_mar_year.append(mar_year)

            print(f"this is reg no  {reg_no}  {place_name} {mar_year}")

        print(missed_data)\

    return missed_reg_no, missed_place_name, missed_mar_year

if __name__ == '__main__':
    missed_data = fetch_missing_data()
    print(f' retrieved  **** {missed_data}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        print('creating ThreadPoolExecutor')
        start_scrape1 = executor.map(my_missed_scraper, missed_data[0], missed_data[1], missed_data[2])
        print('launching ThreadPoolExecutor')


### SCRAP BOOK
# matched_place_name = re.findall("(?<=\\w+_\\w+_)[A-Za-z0-9 ()_.]+(?=_\\d+)", file)
# last_line = re.findall("(?<=.../)[A-Za-z0-9 \\-()_.]+/\\d+/\\d+(?=,)", temp_last_line)
