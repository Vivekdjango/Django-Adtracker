#!/usr/bin/python

import MySQLdb

def insert(data,loc,pf,df):
	d=MySQLdb.connect('localhost','root','mysql','spark')
	c=d.cursor()
	c.execute('INSERT into Image (UI,Profile,C,L) values(%s,%s,%s,%s)',(data,loc,pf,df))
	d.commit()
	c.close()
	return

def bann(data,loc,pf,df):
        d=MySQLdb.connect('localhost','root','mysql','spark')
        c=d.cursor()
        c.execute('INSERT into Banner (UI,Profile,C,L) values(%s,%s,%s,%s)',(data,loc,pf,df))
        d.commit()
        c.close()
        return 

def vid(data,loc,pf,df):
        d=MySQLdb.connect('localhost','root','mysql','spark')
        c=d.cursor()
        c.execute('INSERT into Videos (UI,Profile,C,L) values(%s,%s,%s,%s)',(data,loc,pf,df))
        d.commit()
        c.close()
        return

def carou(data,loc,pf,df):
        d=MySQLdb.connect('localhost','root','mysql','spark')
        c=d.cursor()
        c.execute('INSERT into Carousel (UI,Profile,C,L) values(%s,%s,%s,%s)',(data,loc,pf,df))
        d.commit()
        c.close()
        return

