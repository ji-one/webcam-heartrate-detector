## Project setup

1. Clone project

   ```sh
   $ git clone https://github.com/ji-one/webcam-heartrate-detector.git
   ```

2. 패키지 설치

   ```sh
   $ npm install
   $ pip install -r requirements.txt
   ```

3. `.env` 파일 생성 (secret key, mysql username, password 설정)

   ```
   SECRET_KEY=
   MYSQL_USERNAME=
   MYSQL_PASSWORD=
   ```

4. database 생성

   ```sh
   mysql -u root -p
   mysql> create database whd;
   ```

   

## Run Server

```sh
$ npm run server
$ python ./manage.py runserver
```

➡️ http://localhost:8000 

