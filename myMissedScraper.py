import codecs
import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from check_file import check_file

project_path = 'C:\\Users\\username\\PycharmProjects\\TNregi_Scrape\\'
logs_path = f'{project_path}logs\\'


def my_missed_scraper(start_no, mar_place, mar_year):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    print('loading...\n')

    print(f'--------------> {mar_place}\n')
    print("running myScraper...")

    ########################### SETUP ###########################
    mar_type = 'HMR'
    #start_no = check_file(mar_type, mar_place, mar_year)
    location = mar_place
    year = mar_year  # <
    ########################### SETUP ###########################
    file_path = (f'{project_path}{mar_type}\\{mar_year}\\')
    file_name = f'{file_path}RECORDS_{mar_type}_{location}_{year}.csv'  # FILENAME HERE <----

    print(f'data will be saved to > {file_name}\n')

    driver = webdriver.Chrome(options=options, executable_path='/chromedriver')

    driver.get('https://tnreginet.gov.in/portal/')
    delay = 60  # seconds
    time.sleep(3)
    print('navigating to form...')

    en = driver.find_element_by_xpath('//*[@id="fontSelection"]').click()  # change site to english

    # navigating to form
    more = driver.find_element_by_xpath('//*[@id="1195002"]/a')
    search1 = driver.find_element_by_xpath('//*[@id="8500020"]/a')
    hov_mar = driver.find_element_by_xpath('//*[@id="90000403"]/a')
    hover = ActionChains(driver).move_to_element(more).move_to_element(search1).move_to_element(hov_mar)
    hover.click().perform()

    time.sleep(0.5)  # wait till load
    try:
        myElem = WebDriverWait(driver, delay).until(EC.invisibility_of_element_located((By.ID, 'statusbar')))

        print("Page is ready!")

    except:
        print("navigating took too much time!")
        driver.quit()

    try:

        x = start_no  # looping for each reg number

        print('__________START LOOP__________')

        # filling form
        m_type = driver.find_element_by_xpath('//*[@id="cmb_marrType"]').click()

        if mar_type == 'TMR1':
            sel = driver.find_element_by_xpath('//*[@id="cmb_marrType"]/option[3]').click()  # TN MAR FORM I
        elif mar_type == 'HMR':
            sel = driver.find_element_by_xpath('//*[@id="cmb_marrType"]/option[2]').click()  # HINDU MARRIAGE
        elif mar_type == 'TMR1a':
            sel = driver.find_element_by_xpath('//*[@id="cmb_marrType"]/option[4]').click()  # TN MAR FORM Ia
        elif mar_type == 'SPL':
            sel = driver.find_element_by_xpath('//*[@id="cmb_marrType"]/option[5]').click()  # SPL MAR
        elif mar_type == 'SPLO':
            sel = driver.find_element_by_xpath('//*[@id="cmb_marrType"]/option[6]').click()  # SPL Sadha

        search_by = driver.find_element_by_xpath('//*[@id="Search_Criteria_Two"]')
        hover = ActionChains(driver).move_to_element(search_by)
        hover.click().perform()
        office = driver.find_element_by_xpath('//*[@id="cmb_sub_registrar_office"]').send_keys(location)
        in_reg_no = driver.find_element_by_xpath('//*[@id="RegNO1"]').send_keys(x)
        in_year = driver.find_element_by_xpath('//*[@id="Year"]').send_keys(year)

        submit = driver.find_element_by_xpath('//*[@id="CopyOfMarriageSearch"]/div[2]/div/div[18]/input')
        hover = ActionChains(driver).move_to_element(submit)
        hover.click().perform()  # click submit
        print(f'Loading reg no:         {x}  in   {location}')

        ######    WAIT till page load  ######

        time.sleep(0.5)
        try:
            myElem = WebDriverWait(driver, delay).until(
                EC.invisibility_of_element_located((By.ID, 'statusbar')))  # wait till loading gif disappear
            time.sleep(0.5)
            new_reg_no = driver.find_element_by_xpath('//*[@id="MarriageMstListDisp"]/tbody/tr/td[1]').text
            if res_reg_no == new_reg_no:  # additional wait in case of duplicate old data due to javascript rendering
                time.sleep(3)
            print("table  is ready!")
        except:
            print("Loading table took too much time!")

        ######   EXTRACT DATA FROM TABLE    #####p
        print('Saerching for table to Extract data...')
        res_reg_no = driver.find_element_by_xpath('//*[@id="MarriageMstListDisp"]/tbody/tr/td[1]').text
        res_hus = driver.find_element_by_xpath('//*[@id="MarriageMstListDisp"]/tbody/tr/td[2]').text
        res_wife = driver.find_element_by_xpath('//*[@id="MarriageMstListDisp"]/tbody/tr/td[3]').text
        res_w_par = driver.find_element_by_xpath('//*[@id="MarriageMstListDisp"]/tbody/tr/td[8]').text
        print('Table Found')
        print('-----------------------')
        print(f'|                {location}                 | {res_wife}')
        print('-----------------------')
        # mType.send_keys('- Select -')
        print('start csv write...')
        #####   Insert to CSV FILE   #####
        toAdd = [x, res_reg_no, res_hus, res_wife, res_w_par]
        with open(file_name, "r", encoding='utf-8') as infile:
            reader = list(csv.reader(infile))
            reader.insert((start_no - 1), toAdd)

        with open(file_name, "w", newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            for line in reader:
                writer.writerow(line)
                print('Insert to CSV success !')
                print('**********END**********')


        # with codecs.open(file_name, mode='a', encoding='utf-8') as RECORDS_file:
        #     employee_writer = csv.writer(RECORDS_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #     employee_writer.writerow([x, res_reg_no, res_hus, res_wife, res_w_par])


        driver.quit()


    except:
        driver.quit()
        # if error caused by invalid reg number (reg number not present, max value reached) close the driver
        print('\n \n \n')
        print('+++++++++++++  REQUIRES ATTENTION  +++++++++++++\n')
        print('\n \n \n')
        print('error in ---= >', x)
        with codecs.open(f"{logs_path}Completed_{mar_type}_{year}.txt", mode='a+', encoding='utf-8') as completed_file:
            print('error in --->', x)
            completed_file.write(
                f' Ended at ----->>>>> Place: {mar_place} | loop no: {x} | RegNo: {res_reg_no}| year: {year} \n')
            print(f" Ended at ----->>>>> Place: {mar_place} | loop no: {x} | RegNo: {res_reg_no}| year: {year}    \n")
            print(f'error in ---> {location}', x)
            time.sleep(0.5)
            driver.quit()
        print('error in --->', x)
        print('\n')

        print('error in --->', x)
        driver.quit()

    driver.quit()

# myscraper('TMR1', 1, 'ADAYAR', 2015)   #REMOVE AT END for test run
