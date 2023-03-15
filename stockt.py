#필요한 패키지들 설치
#pip install pandas-datareader
#pip install fix-yaho-finance

# 파이썬 코드
from pandas_datareader import data
import fix_yahoo_finance as yf
import yfinance as yf
yf.pdr_override()


# 삼성전자의 주식 코드와 시작 날짜를 입력합니다.
stock_code1 = "005930.KS"
start_date1 = "2023-03-15"
# 펄어비스
stock_code2 = "263750.KQ"
start_date2 = "2023-03-15"
#한화에어로스페이스
stock_code3 = "012450.KS"
start_date3 = "2023-03-15"
# 야후 파이낸스에서 주식 데이터를 가져옵니다.
samsung = data.get_data_yahoo(stock_code1, start_date1)
pearl= data.get_data_yahoo(stock_code2, start_date2)
hanwha = data.get_data_yahoo(stock_code3, start_date3)
# 가져온 데이터를 확인합니다.
samsung.head() #데이터만 가져왔지 출력은 따로 해줘야함
pearl.head()
hanwha.head()

print("<삼성전자> ",samsung)  #출력
print("<펄어비스> ",pearl)
print("<한화에어로스페이스> ",hanwha)
