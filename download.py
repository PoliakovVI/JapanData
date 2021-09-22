import yfinance as yf

# download data from yahoo.finance
def download_data(yahoo_corp_name="TSLA", output_csv_name="Tesla", download_to_path="", start="2019-01-02", end="2019-12-31", interval='1d'):
	data = yf.download(yahoo_corp_name, start=start, end=end, interval=interval)
	if data.empty:
		return True
	data.to_csv(download_to_path+output_csv_name+".csv")
	return False
	
def read_names():
	f = open('names.txt')
	names = set(f.read().split('\n'))
	f.close()
	return names
	
def write_names(names):
	f = open('names.txt', 'w') 
	buffer = ""
	sep = ""
	for name in names:
		buffer += sep + name
		sep = "\n"
	f.write(buffer)
	f.close()
		
import pandas as pd

def fill_download_list(download_list):
	data = pd.read_csv("stocks_list.csv")
	data = data[ ["Symbol", "Description"] ]
	dwn_list = list()
	for index, row in data.iterrows():
		tiker = row["Symbol"].split(sep=":")[1] + ".T"
		dwn_list.append( [ tiker, row["Description"] ] )
	dwn_list += download_list
	return dwn_list
  
download_list = [  
	["1593.T", "JPX-Nikkei-INDEX"],
	]
	
download_list = fill_download_list(download_list)

download_list = download_list[0:500]

print(len(download_list), "to download")
names = read_names()
id = 1
for item_name in download_list:
	print(item_name[1])
	if item_name[1] not in names:
		if download_data(item_name[0], item_name[1]):
			print("Not found")
		else:
			names.add(item_name[1])
	else:
		print("Already downloaded")
	print(id, "/", len(download_list))
	id += 1

write_names(names)
