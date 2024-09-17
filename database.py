from sqlalchemy import create_engine, text
user = 'root'
password = 'Qwertyuiop123%40'
host = 'localhost'
dbname = 'polito'
db_connection = f"mysql+pymysql://{user}:{password}@{host}/{dbname}?charset=utf8mb4"

engine = create_engine(db_connection)

def load_professors_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from professors"))
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