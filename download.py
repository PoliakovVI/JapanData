import yfinance as yf

# download data from yahoo.finance
def download_data(yahoo_corp_name="TSLA", output_csv_name="Tesla", download_to_path="", start="2019-01-01", end="2019-12-31", interval='1d'):
	data = yf.download(yahoo_corp_name, start=start, end=end, interval=interval)
	data.to_csv(download_to_path+output_csv_name+".csv")
  
download_list = [  
	["TM", "Toyota"],
	["8035.T", "TokyoElectron"],
	["5781.T", "TohoKinzoku"],
	["1593.T", "JPX-Nikkei-INDEX"],
	]

with open("names.txt", 'w') as fout:
	for item_name in download_list:
		download_data(item_name[0], item_name[1])
		fout.write(item_name[1] + "\n")
