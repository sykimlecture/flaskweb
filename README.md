1. pip upgrade
   C:\>python -m pip install --upgrade pip

2. virtualenv 설치
   virtualenv는 가상 Python 환경 빌더.
   virtualenv는 다수의 Python 환경을 생성하도록 해준다. 
   그래서 라이브러리의 다른 버전 사이에서 발생할 수 있는 호환성 문제를 피할 수 있다

3. C:\>pip install virtualenv

4. 프로젝트 디렉토리 생성(Include, Lib, Scripts, tcl 디렉토리 생성됨)
   D:\workspace>virtualenv flaskweb
      Using base prefix 'c:\\python'
      New python executable in D:\workspace\flaskweb\Scripts\python.exe
      Installing setuptools, pip, wheel...done. 

4. Flask 설치
   D:\workspace\flaskweb>pip install Flask

5. mariadb 설치
   D:\workspace\flaskweb>pip install pymysql
   
6. sql 생성
   CREATE TABLE `my_schedule` (
      `id` INT(11) NOT NULL AUTO_INCREMENT,
      `title` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_unicode_ci',
      `start` DATETIME NOT NULL,
      `end` DATETIME NOT NULL,
      `allDay` CHAR(1) NOT NULL DEFAULT 'Y' COLLATE 'utf8mb4_unicode_ci',
      PRIMARY KEY (`id`)
   )
   COLLATE='utf8mb4_unicode_ci'
   ENGINE=InnoDB
   AUTO_INCREMENT=7;

7. 케라스 설치
   D:\workspace\flaskweb>pip install --upgrade keras
   
8. 추가 application 설치
   C:\>pip install requests
