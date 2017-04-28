#!/usr/bin/python

import MySQLdb

def db_image():
        d=MySQLdb.connect('localhost','root','mysql','spark')
        c=d.cursor()
        c.execute('select * from Image')
        i=c.fetchall()
        return i

def db_curr():
	d=MySQLdb.connect('localhost','root','mysql','New')
        c=d.cursor()
        c.execute('select Info,Profile,Location,max(val) from count group by Info,Profile,Location;')
        i=c.fetchall()
        return i

def db_video():
        d=MySQLdb.connect('localhost','root','mysql','spark')
        c=d.cursor()
        c.execute('select * from Videos')
        v=c.fetchall()
        return v

def db_carousel():
        d=MySQLdb.connect('localhost','root','mysql','spark')
        c=d.cursor()
        c.execute('select * from Carousel')
        car=c.fetchall()
        return car

def db_ban():
        d=MySQLdb.connect('localhost','root','mysql','spark')
        c=d.cursor()
        c.execute('select * from Banner')
        b=c.fetchall()
        return b
