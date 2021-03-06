#!/usr/bin/python3
'''
This file was not used in the final implementation - we were
advised to populate from a csv (which turned out to be much easier).

Meant to populate the main database with all legislators from the
2015 CPI dataset. This will return a list of tuples, with each tuple
being:

    lawmaker, state, district, body, corp, industry
'''

import sqlite3

def get_cpi_tuples():
    '''
    Queries just about everything from cpi.db and
    returns a list of tuples. Should be called in views.py
    '''
    query = '''
            SELECT lawmaker,
                   state,
                   district,
                   body,
                   employer_business_interest, 
                   industry
            FROM cpi
            '''
    db = sqlite3.connect('cpi.db')
    db.text_factory = bytes 
    c = db.cursor()
    r = c.execute(query)
    return r.fetchall()

def clean_record(record):
    '''
    Takes in a tuple of byte strings and returns
    a tuple with correct None values in unicode.
    This was necessary becasue some corps were not
    able to query in unicode from the db.
    '''
    last_first = record[0].decode('utf-8').split(',')
    lawmaker = last_first[1][1:] + ' ' + last_first[0]
    state = record[1].decode('utf-8')
    district = record[2].decode('utf-8')
    body = record[3].decode('utf-8')
    try:
        corp = record[4].decode('utf-8')
       # if corp == 'N/A':
        #    corp = None
    except UnicodeDecodeError:
        corp = 'unicode error'
    industry = record[5].decode('utf-8')
    return lawmaker, state, district, body, corp, industry
