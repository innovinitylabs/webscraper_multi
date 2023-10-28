# checks if the registration numbers are n order and if theres any missing data
import codecs
import re
import glob
import os
import concurrent.futures
from itertools import repeat

project_path = 'C:\\Users\\username\\PycharmProjects\\TNregi_Scrape\\'
logs_path = f'{project_path}logs\\'


def check_continuity(mar_type, mar_year):
    file_path = (f'{project_path}{mar_type}\\{mar_year}\\')

    all_files = glob.glob(os.path.join(file_path, "RECORDS_*.csv"))

    print(all_files)

    for file in all_files:
        print(f' checking {file}')
        with open(file, 'r', encoding="utf-8") as f:

            lines = f.readlines()
            #print(f'lines -----> {lines}')
            prev_reg_no = 0
            for line in lines:

                reg_no = re.findall("(?<=\\D\\S/)\\d+(?=/\\d+,)", line)
                place_name = re.findall("(?<=,)\\D+\\d?/\\d+/\\d+(?=,)", line)

                # place_name = re.findall("(?<=.../)[A-Za-z0-9 \\-()_.]+/\\d+/\\d+(?=,)", line) # (?<=,)\D+/\d+/\d+(?=,)
                print(f"this is reg no  {reg_no}")
                r_no = int(reg_no[0])

                if r_no <= (prev_reg_no + 1):
                    print(f' no data missing between {prev_reg_no} & {r_no} in {mar_type} - {place_name}\n')
                    prev_reg_no = r_no

                else:
                    print(f'data missing between {prev_reg_no} & {r_no} in {mar_type} - {place_name}\n')

                    with codecs.open(f"{logs_path}Continuity_check_{mar_type}_{mar_year}.txt", mode='a') as conty_file:
                        conty_file.write(f'data missing between {prev_reg_no} & {r_no} in {mar_type} - {place_name}\n')
                        print('Write to logs success !')

                    prev_reg_no = r_no


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
        print('creating ThreadPoolExecutor')
        p = ('HMR', 'TMR1')
        year = (2015, 2016, 2017)
        start_scrape1 = executor.map(check_continuity, [i for i in p for j in year], year * len(p))



#### Scrapbook
# check_continuity('TMR1', 2015)
# time.sleep(3)
# check_continuity('TMR1', 2016)
# time.sleep(3)
# check_continuity('TMR1', 2017)
# time.sleep(3)
#  
# check_continuity('HMR', 2016)
# time.sleep(3)
# check_continuity('HMR', 2017)


# matched_place_name = re.findall("(?<=\\w+_\\w+_)[A-Za-z0-9 ()_.]+(?=_\\d+)", file)

# last_line = re.findall("(?<=.../)[A-Za-z0-9 \\-()_.]+/\\d+/\\d+(?=,)", temp_last_line)
