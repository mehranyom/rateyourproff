from sqlalchemy import create_engine, text

user = 'root'
password = 'Qwertyuiop123%40'
host = 'localhost'
dbname = 'polito'
db_connection = f"mysql+pymysql://{user}:{password}@{host}/{dbname}?charset=utf8mb4"



engine = create_engine(db_connection)


def load_professors_from_db():
    query = text("""
            SELECT *
            FROM PROFESSORS
        """)
    with engine.connect() as conn:
        result = conn.execute(query)
        result_all = result.mappings().all()
        return result_all
    
def load_professor_course_from_db(pid):
    query = text("""
        SELECT DISTINCT CName
        FROM teaches t, course c
        WHERE t.CID = c.CID AND PID = :PID
    """)
    with engine.connect() as conn:
        result = conn.execute(query, {"PID": pid})
        result_all = [row[0] for row in result]
        return result_all

def load_all_course_from_db():
    query = text("""
        SELECT DISTINCT CName
        FROM course
    """)
    with engine.connect() as conn:
        result = conn.execute(query)
        result_all = result.mappings().all()
        return result_all


def store_rating_into_db(pid, data):
    with engine.connect() as conn:
        add_rating = text("""
            INSERT INTO RATING(PID, TQuality, Grading, Ethic, TLoad)
            VALUES (:PID, :TQuality, :Grading, :Ethic, :TLoad)
        """)
        
        data_rating = {
            'PID': pid,
            'TQuality': data['teaching_quality'],
            'Grading': data['grading'],
            'Ethic': data['ethic'],
            'TLoad': data['teaching_load']
        }
        
        conn.execute(add_rating, data_rating)
        conn.commit()