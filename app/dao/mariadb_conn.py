# import urllib from urllib.request import urlopen
import json
import pymysql


# db 연결을 담당할 함스
def get_connection():
    return pymysql.connect(host='x.x.x.x', user='x', password='x', db='x', charset='utf8')


# select한 데이터중 mysql datetime 형식의 값을 fullCalendar 에서 처리할수 있도록 포멧 변경
def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


# sql 중복 부분 리팩토링
def sql_template(type, sql, params=None):
    # Connection 연결
    connetion = get_connection()
    try:
        #insert, update, delete 사용
        if type == 3 :
            with connetion.cursor() as cursor :
                # 데이터 입력
                rows = cursor.execute(sql, params)
                # commit
                connetion.commit()
                return rows
        else :
            # 1 = fetchall() 2 = fetchone()
            with connetion.cursor(pymysql.cursors.DictCursor) as cursor :
                # SQL 처리
                cursor.execute(sql, params)
                # 처리된 data 가져옴
                if type == 1 :
                    return cursor.fetchall()
                elif type == 2 :
                    return cursor.fetchone()
    finally:
        # Connection 닫기
        connetion.close()


# 등록된 schedule을 가져옴
def get_scheduler(searchDate):
    if not parameter_checker(searchDate) :
        return json.dumps({})
    sql = "select id, title, start, end, if(allDay = %s,true,false) allDay from my_schedule where to_days(start) >= to_days(%s) and to_days(end) <= to_days(%s)"
    params = ('Y', searchDate['start'], searchDate['end'])
    #처리된 데이터를 json으로 변경 datetime처리를 위해 date_handler지정
    return json.dumps(sql_template(1, sql, params), default=date_handler);


# 넘어온 schedule을 등록
def set_scheduler(schedule):
    #넘어온 데이터중 빈값이 있으면 0 리턴
    if not parameter_checker(schedule) :
        return json.dumps({'rows' : 0})
    else :
        sql = "INSERT INTO my_schedule(title, start, end, allDay) VALUES (%s, %s, %s, %s)"
        params = (schedule['title'], schedule['start'], schedule['end'], schedule['allDay'])
        return json.dumps({'rows' : sql_template(3, sql, params)})


# schedule 삭제
def del_scheduler(id):
    #넘어온 데이터중 빈값이 있으면 0 리턴
    if not parameter_checker(id) :
        return json.dumps({'rows' : 0})
    else :
        sql = "DELETE FROM my_schedule WHERE id = %s"
        params = (id)
        return json.dumps({'rows' : sql_template(3, sql, params)})


# 넘어온 schedule id에 해당하는 schedule을 수정
def put_scheduler(schedule):
    # 넘어온 데이터중 빈값이 있으면 0 리턴
    if not parameter_checker(schedule) :
        return json.dumps({'rows' : 0})
    else :
        sql = "UPDATE my_schedule SET title = %s, start = %s, end = %s, allDay = %s WHERE id = %s"
        params = (schedule['title'], schedule['start'], schedule['end'], schedule['allDay'], schedule['id'])
        return json.dumps({'rows' : sql_template(3, sql, params)})


# parameter 빈값 확인
def parameter_checker(params):
    #0이거나 공백일경우 false
    if not bool(params):
        return False
    #str 이나 unicode일경우 trim 된 문자열이 공백인지 확인
    elif hasattr(params,'strip') and not bool(params.strip()):
            return False
    # Dictoionary형식의 타입 체크
    elif hasattr(params,'values'):
        for value in params.values() :
            if not parameter_checker(value) :
                return False
        return True
    else:
        return True
