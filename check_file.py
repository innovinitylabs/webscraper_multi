# checks if the file exists and returns from where to start the scraping for that file/place

import codecs
import pathlib
import re

project_path = 'C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\'
logs_path = f'{project_path}logs\\'


def check_file(mar_type, mar_place, mar_year) -> int:
    place_name = mar_place
    file_path = (f'{project_path}{mar_type}\\{mar_year}\\')
    new_file_name = f'{file_path}RECORDS_{mar_type}_{place_name}_{mar_year}.csv'
    if pathlib.Path(new_file_name).is_file():
        print('file exist')
        print('extracting last lines...')

        # all_files = glob.glob(os.path.join(yr_path, f"RECORDS_*_.csv"))  # change here
        # print(all_files)
        # for file in all_files:
        #     print(file)
        #
        #     matched_place_name = re.findall("(?<=\\w+_\\w+_)[A-Za-z0-9 ()_.]+(?=_\\d+)", file)
        #
        #     print(f'Regex result -------- >{matched_place_name}')

        with open(new_file_name, 'r', encoding="utf-8") as f:
            temp_last_line = f.readlines()[-1]
            print(f'temp last line {temp_last_line}')
            last_line = re.findall("(?<=.../)[A-Za-z0-9 \\-()_.]+/\\d+/\\d+(?=,)", temp_last_line)

            print(f"this is {last_line}")
            with codecs.open(f"{logs_path}LastLines_{mar_year}.txt",
                             mode='a') as lastLine_file:
                final_out = last_line[0].split("/", 3)
                lastLine_file.write(f"{last_line[0]}\n")
                print('Write last line to file success !')
                print(f' {final_out[0]} has details till {final_out[1]} ')
                return int(final_out[1]) + 1

                # verify(matched_place_name[0], final_out[1], final_out[2])
    else:
        start_no = 1
        print(f'{place_name} is fresh run')
        return 1


#print(check_file('TMR1', 'ambattur', 2015))
