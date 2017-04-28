#!/usr/bin/python

import MySQLdb


def db_bar():
        d=MySQLdb.connect('localhost','root','mysql','spark')
        c=d.cursor()
        c.execute('select * from PSO')
        p=c.fetchall()
        return p[1:]

