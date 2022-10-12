import datetime
from configparser import ConfigParser

import psycopg2

from partner_records.models import DoctorNotes, PartnerRecord


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def config(filename='partner-database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def query_partner_records(self, partner):
    conn = psycopg2.connect(
        host="localhost",
        database="partner",
        user="partner",
        password="partner")

def count_partner_patient_data_records():
    conn = psycopg2.connect(
        host="localhost",
        database="partner",
        user="partner",
        password="partner")

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM patient_data")
    result = cur.fetchall()

    print(f"{result[0][0]} records in the patient_data table")
    return result[0][0]

def count_partner_doctor_notes():
    conn = psycopg2.connect(
        host="localhost",
        database="partner",
        user="partner",
        password="partner")

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM partner_doctor_note")
    result = cur.fetchall()

    print(f"{result[0][0]} records in the doctor_notes table")

    return result[0][0]

def fetch_partner_doctor_notes():
    conn = psycopg2.connect(
        host="localhost",
        database="partner",
        user="partner",
        password="partner")

    cur = conn.cursor()
    cur.execute("SELECT * FROM partner_doctor_note")
    result = cur.fetchall()

    for row in result:
        new_note = DoctorNotes(title=row[1],summary='fetched from remote on ' + str(datetime.datetime.utcnow()) + ' by ' + __name__, body=row[3])
        new_partner_record = PartnerRecord(partner_name='TGIF', doctor_notes=new_note)

        new_note.save()
        new_partner_record.save()

    return len(result)

def connect( params=None):
    """ Connect to the PostgreSQL database server """
    conn = psycopg2.connect(
        host="localhost",
        database="partner",
        user="partner",
        password="partner")

    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # print('Patient table:')
        # cur.execute('SELECT * FROM patient_data')
        # print(cur.fetchall())

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

