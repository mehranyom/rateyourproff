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
    