import psycopg2

try: 
    conn = psycopg2.connect(
                            host = '',
                            dbname = '',
                            user = '',
                            password = '',
                            port = 5432
    )

    cur = conn.cursor()

    create_script = """ CREATE TABLE IF NOT EXISTS person (
                id INT PRIMARY KEY,
                name VARCHAR(255),
                age INT
        )
    """
    cur.execute(create_script)
    conn.commit()
    
except Exception as e:
    print(e)
finally: 
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()