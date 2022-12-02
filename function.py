import mysql.connector
import streamlit as st
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ya@636156",
    
)
c=mydb.cursor()
def table_create():
    c.execute("CREATE DATABASE IF NOT EXISTS DISEASE")
    c.execute("CREATE TABLE IF NOT EXISTS DISEASE.USER_LOGIN(USER_ID VARCHAR(20),PASSWORD VARCHAR(20))")


def user_login_check(id,password):
    table_create()
    c.execute("SELECT*FROM DISEASE.USER_LOGIN WHERE DISEASE.USER_LOGIN.USER_ID='{}' AND USER_LOGIN.PASSWORD='{}'".format(id,password))
    result=c.fetchall()
    if result:
        return 1
    else:
        return 0
        

def user_signup(id,password):
    table_create()
    c.execute("INSERT INTO DISEASE.USER_LOGIN VALUES('{}','{}')".format(id,password))
    mydb.commit()
    
    

def user_signup_check(id):
    table_create()
    c.execute("SELECT*FROM DISEASE.USER_LOGIN WHERE DISEASE.USER_LOGIN.USER_ID='{}'".format(id))
    result=c.fetchall()
    if result:
        return 1
    else:
        return 0