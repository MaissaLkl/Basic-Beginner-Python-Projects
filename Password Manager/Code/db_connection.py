import psycopg2

def get_connection():
    try: 
        conn = psycopg2.connect(
                                host = '',
                                dbname = '',
                                user = '',
                                password = '',
                                port = 
        )
        return conn
    except psycopg2.DatabaseError as error:
        print(f"Error occurred: {error}")
        return None