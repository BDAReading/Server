# Server

### 현재 폴더 구조

```yaml
BookReviewApp
│   requirements.txt # Python 의존성 목록 파일
│
├───app
│   │   config.py # 여러 기능 함수들을 넣고 관리하는 파일
│   │   database.py # DB 연동 파일
│   │   main.py # 서버 실행 파일
│   │   models.py # ORM 모델 관리 파일
│   │   schemas.py # pydantic 모델 관리 파일
```

<br>
* git clone 하시면 secrets.json 파일을 만들어서 DB 경로를 지정하면 됩니다.
* 가상환경은 venv 사용.