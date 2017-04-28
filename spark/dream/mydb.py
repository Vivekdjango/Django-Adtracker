#!/usr/bin/python

import MySQLdb

def mydb():
        d=MySQLdb.connect('localhost','root','mysql','New')
        c=d.cursor()
        c.execute('select * from XX_SAMPLE')
        p=c.fetchall()
        return p
