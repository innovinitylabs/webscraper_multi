import glob, os

y2015 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\HMR\\2015"
y2016 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\HMR\\2015"
y2017 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\HMR\\2015"

TN_ma_f1_2015 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\TMR1\\2015"
TN_ma_f1_2016 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\TMR1\\2016"
TN_ma_f1_2017 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\TMR1\\2017"


TN_ma_f1a_2015 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\TMR1a\\2015"
TN_ma_f1a_2016 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\TMR1a\\2016"
TN_ma_f1a_2017 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\TMR1a\\2017"

CMR_2015 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\CMR\\2015"
CMR_2016 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\CMR\\2016"
CMR_2017 = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\CMR\\2017"


mergedFolder = "C:\\Users\\Shyam\\PycharmProjects\\TNregi_Scrape\\"

print('merging 2015.....')

all_files = glob.glob(os.path.join(y2015, "RECORDS_*.csv"))
with open("Merged 2015 v2.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged 2015 !')


print('merging 2016.....')

all_files = glob.glob(os.path.join(y2016, "RECORDS_*.csv"))
with open("Merged 2016 v2.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged 2016 !')


print('merging 2017.....')

all_files = glob.glob(os.path.join(y2017, "RECORDS_*.csv"))
with open("Merged 2017 v2.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged 2017 !')



# TAMILNADU MARRIAGE FORM I
print('merging TN_ma_f1 2015.')

all_files = glob.glob(os.path.join(TN_ma_f1_2015, "RECORDS_*.csv"))
with open("Merged 2015 TN_ma_f1_2015.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged TN_ma_f1 2015 !')

print('merging TN_ma_f1 2016.')

all_files = glob.glob(os.path.join(TN_ma_f1_2016, "RECORDS_*.csv"))
with open("Merged 2016 TN_ma_f1_2016.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged TN_ma_f1 2016 !')


print('merging TN_ma_f1 2017.')

all_files = glob.glob(os.path.join(TN_ma_f1_2017, "RECORDS_*.csv"))
with open("Merged 2017 TN_ma_f1_2017.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged TN_ma_f1 2017 !')



# TAMILNADU MARRIAGE FORM Ia
print('merging TN_ma_f1a_2015 .')

all_files = glob.glob(os.path.join(TN_ma_f1a_2015, "RECORDS_*.csv"))
with open("Merged 2015 TN_ma_f1a_2015.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged TN_ma_f1a 2015 !')

print('merging TN_ma_f1a 2016.')

all_files = glob.glob(os.path.join(TN_ma_f1a_2016, "RECORDS_*.csv"))
with open("Merged 2016 TN_ma_f1a_2016.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged TN_ma_f1a 2016 !')


print('merging TN_ma_f1a 2017.')

all_files = glob.glob(os.path.join(TN_ma_f1a_2017, "RECORDS_*.csv"))
with open("Merged 2017 TN_ma_f1a_2017.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged TN_ma_f1a 2017 !')





# CHRISTIAN MARRIAGE
print('merging CMR 2015.')

all_files = glob.glob(os.path.join(CMR_2015, "RECORDS_*.csv"))
with open("Merged 2015 CMR_2015.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged CMR 2015 !')

print('merging CMR 2016.')

all_files = glob.glob(os.path.join(CMR_2016, "RECORDS_*.csv"))
with open("Merged 2016 CMR_2016.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged CMR 2016 !')


print('merging CMR 2017.')

all_files = glob.glob(os.path.join(CMR_2017, "RECORDS_*.csv"))
with open("Merged 2017 CMR_2017.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged CMR 2017 !')





print('MERGING All.....')

all_files = glob.glob(os.path.join(mergedFolder, "Merged 20*.csv"))
with open("MAR REC 2015-17.csv", "wb") as outfile:
	for f in all_files:
		with open(f, "rb") as infile:
			outfile.write(infile.read())
print('merged All !')