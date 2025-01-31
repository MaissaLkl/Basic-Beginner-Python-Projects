import psycopg2
from db_connection import get_connection

def create_table():
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            create_script = """ CREATE TABLE IF NOT EXISTS Manager (
                        App_Name TEXT ,
                        URL TEXT,
                        Username TEXT,
                        Email TEXT,
                        Password TEXT
                )
            """
            cur.execute(create_script)
            conn.commit()
        except psycopg2.DatabaseError as error:
            print(f"Error occurred: {error}")
            conn.rollback()
        finally: 
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()

def insert_db(app= None, url= None, usr= None, email= None, pwd= None):
    if app is None and url is None or usr is None or email is None or pwd is None:
        raise ValueError('Please provide all necessary information.')
    
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            if app is not None:
                insert_script = """ INSERT INTO Manager (App_Name, Username, Email, Password) VALUES (%s,%s,%s,%s)"""
                cur.execute(insert_script, (app, usr, email, pwd))
            elif url is not None:
                insert_script = """ INSERT INTO Manager (URL, Username, Email, Password) VALUES (%s,%s,%s,%s)"""
                cur.execute(insert_script, (url, usr, email, pwd))
            
            conn.commit()
        except psycopg2.DatabaseError as error:
            print(f"Error occurred: {error}")
            conn.rollback()
        finally: 
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


def delete_db(app = None, url = None):
    if app is None and url is None:
        raise ValueError('Please provide all necessary information.')
        
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            if app is not None:
                delete_script = """ DELETE FROM Manager WHERE App_Name = %s"""
                cur.execute(delete_script, (app,))
            elif url is not None: 
                delete_script = """ DELETE FROM Manager WHERE URL = %s"""
                cur.execute(delete_script, (url,))
            
            conn.commit()
        except psycopg2.DatabaseError as error:
            print(f"Error occurred: {error}")
            conn.rollback()
        finally: 
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()

def select_pwd_db(app= None, url= None):
    if app is None and url is None:
        raise ValueError('Please provide all necessary information.')
    
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            if app is not None:
                printpwd_script = """ SELECT Password FROM Manager WHERE App_Name = %s"""
                cur.execute(printpwd_script, (app,))
            elif url is not None:
                printpwd_script = """ SELECT Password FROM Manager WHERE URL = %s"""
                cur.execute(printpwd_script, (url,))
            
            result = cur.fetchone()
            
            if result is not None:
                return str(result[0])
            else:
                print('No result found.')
            
        except psycopg2.DatabaseError as error:
            print(f"Error occurred: {error}")
            conn.rollback()
        finally: 
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


def select_db(app = None, url= None):
    if app is None and url is None:
        raise ValueError('Please provide all necessary information.')
    
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            if app is not None:
                print_script = """ SELECT * FROM Manager WHERE App_Name = %s"""
                cur.execute(print_script, (app,))
            elif url is not None:
                print_script = """ SELECT * FROM Manager WHERE URL = %s"""
                cur.execute(print_script, (url,))
            
            result = cur.fetchall()
            
            if result is not None:
                return result
            else:
                print('No results found.')
                
        except psycopg2.DatabaseError as error:
            print(f"Error occurred: {error}")
            conn.rollback()
        finally: 
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


def update_pwd_db(app= None, url= None, pwd= None):
    if app is None and url is None or pwd is None:
        raise ValueError('Please provide all necessary information.')
    
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            if app is not None:
                updatepwd_script = """ UPDATE Manager SET Password = %s WHERE App_Name = %s"""
                cur.execute(updatepwd_script, (pwd, app,))
            elif url is not None:
                updatepwd_script = """ UPDATE Manager SET Password = %s WHERE URL = %s """
                cur.execute(updatepwd_script, (pwd, url,))
            
            conn.commit()
        except psycopg2.DatabaseError as error:
            print(f"Error occurred: {error}")
            conn.rollback()
        finally: 
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


def update_usr_db(app= None, url= None, usr= None):
    if app is None and url is None or usr is None:
        raise ValueError('Please provide all necessary information.')
    
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            if app is not None:
                updateusr_script = """ UPDATE Manager SET Username = %s WHERE App_Name = %s"""
                cur.execute(updateusr_script, (usr, app,))
            elif url is not None: 
                updateusr_script = """ UPDATE Manager SET Username = %s WHERE URL = %s"""
                cur.execute(updateusr_script, (usr, url,))
            
            conn.commit()
        except psycopg2.DatabaseError as error:
            print(f"Error occurred: {error}")
            conn.rollback()
        finally: 
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


def update_email_db(app = None, url = None, email= None):
    if app is None and url is None or email is None:
        raise ValueError('Please provide all necessary information.')
    
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            if app is not None:
                updateemail_script = """ UPDATE Manager SET Email = %s WHERE App_Name = %s """
                cur.execute(updateemail_script, (email, app,))
            elif url is not None:
                updateemail_script = """ UPDATE Manager SET Email = %s WHERE URL = %s """
                cur.execute(updateemail_script, (email, url,))
            
            conn.commit()
        except psycopg2.DatabaseError as error:
            print(f"Error occurred: {error}")
            conn.rollback()
        finally: 
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


def update_app_db(app1 = None, app2 = None, url = None):
    if app2 is None and url is None or app1 is None:
        raise ValueError('Please provide all necessary information.')
    
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            if app2 is not None:
                updateapp_script = """ UPDATE Manager SET App_Name = %s WHERE App_Name = %s"""
                cur.execute(updateapp_script, (app1, app2,))
            elif url is not None:
                updateapp_script = """ UPDATE Manager SET App_Name = %s WHERE URL = %s"""
                cur.execute(updateapp_script, (app1, url,))
            
            conn.commit()
        except psycopg2.DatabaseError as error:
            print(f"Error occurred: {error}")
            conn.rollback()
        finally: 
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


def update_url_db(app = None, url1 = None, url2 = None):
    if app is None and url2 is None or url1 is None:
        raise ValueError('Please provide all necessary information.')
    conn = get_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            if app is not None:
                updateurl_script = """ UPDATE Manager SET URL = %s WHERE App_Name = %s"""
                cur.execute(updateurl_script, (url1, app,))
            elif url2 is not None:
                updateurl_script = """ UPDATE Manager SET URL = %s WHERE URL = %s"""
                cur.execute(updateurl_script, (url1, url2,))
            
            conn.commit()
        except psycopg2.DatabaseError as error:
            print(f"Error occurred: {error}")
            conn.rollback()
        finally: 
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


    