# REST_API_with_Django
### Django REST framework 를 통한 날씨 정보 api 제공

**파이썬 크롤링으로 데이터 수집 + DB 업로드와  
파이썬 장고의 레스트 프레임워크를 사용해, rest API 를 pythonanywhere 로 배포**

>아래 repo 와 연결됩니다.  
https://github.com/Kimdonghyeon7645/ScienceProject

개발 기간은 2020-5-9(오후 9시) ~ 2020-5-10(오전 0시)    
(순수 개발시간은 중간에 코딩하다말고 딴일 하고 온꺼 빼면 1~2시간정도.)

### 결과

현재 로컬로 구현을 완료했으며, (2020-5-9)  
pythonanywhere 에서 배포했음 (2020-5-10)

테스트 :  
http://weatherapi.pythonanywhere.com/gu/hi

유성구 날씨 :  
http://weatherapi.pythonanywhere.com/gu/0  
서구 날씨 :  
http://weatherapi.pythonanywhere.com/gu/1  
중구 날씨 :  
http://weatherapi.pythonanywhere.com/gu/2  
대덕구 날씨 :  
http://weatherapi.pythonanywhere.com/gu/3  
동구 날씨 :  
http://weatherapi.pythonanywhere.com/gu/4  

헤더정보 (해당 데이터의 업로드 시각) :  
http://weatherapi.pythonanywhere.com/gu/header


그리고 DB를 매일마다 그날 그날의 날씨정보를 업데이트 할 수 있게,   
task 에 크롤링 + DB 업로드를 자동화할 수 있는 코드를 작성+추가.

---

예전에 하던 과학 프로젝트의 연장선이라서 쉽게(실 개발시간 3시간 내외) 끝낼 수 있었다!  
여기서 더욱 공부해서 제대로 된 문법을 다져야 겠다... 
