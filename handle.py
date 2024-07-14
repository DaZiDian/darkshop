import configparser  
import mysql.connector  
import sqlite3  
import pymssql  
from pymongo import MongoClient  
import redis  
  
def get_database_connection(config_file='config.ini'):  
    config = configparser.ConfigParser()  
    config.read(config_file)  
      
    database_type = config['DEFAULT']['database_type'].lower()  
      
    if database_type == 'mysql':  
        return mysql.connector.connect(  
            host=config['MySQL']['host'],  
            user=config['MySQL']['user'],  
            password=config['MySQL']['password'],  
            database=config['MySQL']['database']  
        )  
    elif database_type == 'sqlite':  
        return sqlite3.connect(config['SQLite']['path'])  
    elif database_type == 'sqlserver':  
        return pymssql.connect(  
            server=config['SQLServer']['server'],  
            user=config['SQLServer']['username'],  
            password=config['SQLServer']['password'],  
            database=config['SQLServer']['database']  
        )  
    elif database_type == 'mongodb':  
        return MongoClient(  
            host=config['MongoDB']['host'],  
            port=int(config['MongoDB']['port']),  
            username=None,  # Add username if needed  
            password=None,  # Add password if needed  
            authSource=config['MongoDB']['database']  
        )[config['MongoDB']['database']]  
    elif database_type == 'redis':  
        return redis.Redis(  
            host=config['Redis']['host'],  
            port=int(config['Redis']['port']),  
            db=int(config['Redis']['db'])  
        )  
    else:  
        raise ValueError("Unsupported database type: {}".format(database_type))  
  
# 使用示例  
conn = get_database_connection()  
# 根据conn的类型执行相应的数据库操作...