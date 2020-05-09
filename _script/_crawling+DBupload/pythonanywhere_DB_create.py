# -*- coding: utf-8 -*-
"""
2020-5-10
유빈이와 프로젝트로 또 쓰게된 코드다. 
간단하게 pythonanywhere 원격 DB에 업로드할 코드를 출력한다.
복붙해서 그대로 db 콘솔에 넣어주자.
"""
from bs4 import BeautifulSoup
import requests


pms = [['보통', '보통'], ['보통', '보통'], ['보통', '보통']]
# url2 = 'https://www.airkorea.or.kr/web/dustForecast?pMENU_NO=113'
# html2 = requests.get(url2)
# soup2 = BeautifulSoup(html2.text, 'html.parser')
# contents2 = soup2.select("dl.forecast.MgT50")
# for content2 in contents2:
#     cols = content2.select("table.st_2 tbody tr")
#     try:
#         big_pm = num_change(cols[1].select("td")[6].text)
#     except IndexError:
#         big_pm = 'NoneData'
#     # 미세먼지
#     try:
#         small_pm = num_change(cols[2].select("td")[6].text)

#     except IndexError:
#         small_pm = 'NoneData'
#     # 초미세먼지
#     pm = [big_pm, small_pm]
#     pms.append(pm)


all_data = []
header = []
num = 1
urls = [
    'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3020055000',  # 유성구 (신성동)
    'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3017059700',  # 서구 (관저동)
    'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3014074000',  # 중구 (산성동)
    'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3023060000',   # 대덕구 (법동)
    'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3011062000'   # 동구 (가양동)
]

for gu, url in enumerate(urls):  # 유성구, 서구, 중구, 대덕구, 동구순
    num = 1
    gu_data = []
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    # header 행
    if not header:
        n = str(1)  # 헤더 테이블 행 번호
        update_year = soup.find('tm').text[:4]
        update_month = soup.find('tm').text[4:6]
        update_date = soup.find('tm').text[6:8]
        update_time = soup.find('tm').text[8:-2]
        header = [n, update_year, update_month, update_date, update_time]

    contents = soup.select('data')
    for content in contents:
        hour = content.find('hour').text  # 현재 시간 (3시간 간격, ex> 3, 6, 9, ...)
        day_num = int(content.find('day').text)
        time_difference = str(int(hour) - int(update_time) + int(day_num)*24)  # 시간 차이
        temp = content.find('temp').text  # 현재 온도 (섭씨 ℃)
        day_high_temp = content.find('tmx').text  # 현재 날짜의 최고 온도 (오늘은 구하지 않음, -999)
        day_low_temp = content.find('tmn').text  # 현재 날짜의 최저 온도 (오늘은 구하지 않음, -999)
        sky_state = content.find('sky').text  # 현재 하늘의 상태, 구름의 정도 1~4로 표현(1:맑음, 2:구름적음, 3:구름많음, 4:흐림)
        weather_state = content.find('pty').text  # 현재 기상현상 상태, 0: 맑음, 1: 비, 2: 진눈개비, 3: 눈, 4: 소나기
        weather_kor = content.find('wfkor').text  # 현재 기상현상 상태 통틀어서 한글로 (대문자 태그 안됌)
        rain_persent = content.find('pop').text  # 현재 비올 확률 (백분위, %)
        expect_rain_6h = content.find('r06').text  # 6시간 뒤까지의 예상 강수량
        expect_rain_12h = content.find('r12').text  # 12시간 뒤까지의 예상 강수량
        expect_snow_6h = content.find('s06').text  # 6시간 뒤까지의 예상 적설량
        expect_snow_12h = content.find('s12').text  # 12시간 뒤까지의 예상 적설량
        wind_speed = str(round(float(content.find('ws').text), 2))  # 현재 풍속
        wind_way = content.find('wd').text  # 현재 풍향(8분위, ex> 0: 북, 2: 동, 4: 남, 6: 서)
        wind_korean = content.find('wden').text  # 현재 풍향 한글로
        humi = content.find('reh').text  # 현재 습도 (백분위, %)
        hour_data = [
            str(num), gu, time_difference, hour, temp, day_high_temp, day_low_temp, sky_state, weather_state, weather_kor,
            rain_persent, expect_rain_6h, expect_rain_12h, expect_snow_6h, expect_snow_12h, wind_speed, wind_way,
            wind_korean, humi, pms[int(day_num)][0], pms[int(day_num)][1]
        ]
        num += 1
        gu_data.append(hour_data)
    all_data.append(gu_data)

# -*- 크롤링 끝, pythonanywhere 원격 DB 업로드 시작 -*-

database_name = "pj_db"
user_name = 'bosal'
user_password = 'kkddhh77887788@'
pythonanywhereDatabaseHostname = 'bosal.mysql.pythonanywhere-services.com'

# conn = mysql.connector.connect(
#     user=user_name, password=user_password,
#     host=pythonanywhereDatabaseHostname, port=3306,
#     database=f'{user_name}${database_name}',
# )
# cur = conn.cursor()
# header 테이블 생성 출력
print(
    "CREATE TABLE header( num TINYINT, update_year INT, update_month TINYINT, update_date TINYINT, "
    "update_time TINYINT, PRIMARY KEY(num) );"
)
print("INSERT INTO header(num, update_year, update_month, update_date, update_time) VALUES (", end='')
for i, yo_so in enumerate(header):
    if i is 0:
        print("'", yo_so, "'", sep='', end='')
    else:
        print(", '", yo_so, "'", sep='', end='')
print(");")

# 구별로 테이블 생성 + 삽입문 출력
for index, gu_data in enumerate(all_data):
    print(
        f"CREATE TABLE gu_{index} (num TINYINT, gu TINYINT, time_difference TINYINT, hour TINYINT, temp SMALLINT, "
        f"day_high_temp SMALLINT, day_low_temp SMALLINT, sky_state TINYINT, weather_state TINYINT, "
        f"weather_kor VARCHAR(20), rain_persent TINYINT, expect_rain_6h FLOAT, expect_rain_12h FLOAT, "
        f"expect_snow_6h FLOAT, expect_snow_12h FLOAT, wind_speed FLOAT, wind_way TINYINT, wind_text CHAR(4), "
        f"humi TINYINT, fine_dust VARCHAR(10), small_fine_dust VARCHAR(10), PRIMARY KEY(num) );"
    )
    for data in gu_data:
        print(
            f"INSERT INTO gu_{index} (num, gu, time_difference, hour, temp, day_high_temp, day_low_temp, "
            f"sky_state, weather_state, weather_kor, rain_persent, expect_rain_6h, expect_rain_12h, "
            f"expect_snow_6h, expect_snow_12h, wind_speed, wind_way, wind_text, humi, fine_dust, small_fine_dust) "
            f"VALUES ("
        )
        for i, yo_so in enumerate(data):
            if i is 0:
                print("'", yo_so, "'", sep='', end='')
            else:
                print(", '", yo_so, "'", sep='', end='')
        print(");")
#     conn.commit()
# cur.close()
# conn.close()
