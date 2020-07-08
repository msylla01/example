import sqlite3
from sqlite3 import Error
from classes.Classes import Client

import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create database and insert
conn = sqlite3.connect('restorapid_db.db')
c = conn.cursor()


def create_item(article):
    sql = ''' INSERT INTO Articles(article_id,name,total_item_price,price,instruction, type,type_id,item_discount, cart_discount_rate,cart_discount,tax_type)
        VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    try:
        c.execute("SELECT * FROM Articles")
        rows = c.fetchall()
        if not rows:
            c.execute(sql, article)
            conn.commit()
            return c.lastrowid
        else:
            for row in rows:
                if row[1] == article[1]:
                    print('article existe')
                else:
                    c.execute(sql, article)
                    conn.commit()
                    return c.lastrowid
    except Error as a:
        print(a)


def create_option(option):
    sql = ''' INSERT INTO Options(name,price,group_name,quantite , type, type_id)
        VALUES(?,?,?,?,?,?) '''
    try:
        c.execute("SELECT * FROM Options")
        rows = c.fetchall()
        if not rows:
            c.execute(sql, option)
            conn.commit()
            return c.lastrowid
        else:
            for row in rows:
                if row[1] == option[1]:
                    print('option existe')
                else:
                    c.execute(sql, option)
                    conn.commit()
                    return c.lastrowid
    except Error as a:
        print(a)


def create_order(commande):
    sql = ''' INSERT INTO Commande(client_id, restaurant_id, prix_total, nombre_article, type, status, source, accepted_at, fulfill_at,instructions,tax_value,currency,payment)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    try:
        c.execute("SELECT * FROM Commande")
        rows = c.fetchall()
        if not rows:
            c.execute(sql, commande)
            conn.commit()
            return c.lastrowid
        else:
            for row in rows:
                c.execute(sql, commande)
                conn.commit()
                return c.lastrowid
    except Error as a:
        print(a)


def create_resto(restaurant):
    sql = ''' INSERT INTO Restaurant(resto_id,nom,phone,pays,ville,adresse,latitude,longitude,restaurant_token,restaurant_zipcode)
        VALUES(?,?,?,?,?,?,?,?,?,?) '''
    try:
        c.execute("SELECT * FROM Restaurant")
        rows = c.fetchall()
        if not rows:
            c.execute(sql, restaurant)
            conn.commit()
            return c.lastrowid
        else:
            for row in rows:
                if row[1] == restaurant[1]:
                    print ('resto existe')
                else:
                    c.execute(sql, restaurant)
                    conn.commit()
                    return c.lastrowid
    except Error as a:
        print(a)


def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def update_nombre_commande_client():
    c.execute("SELECT * FROM Client")
    rows = c.fetchall()
    for row in rows:
        Client.update_client_final((0, row[0]))


# update_nombre_commande_client()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS Options(
            id integer primary key not null,
            name text,
            price integer,
            group_name text,
            quantite integer,
            type text,
            type_id integer
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS Articles(
            id integer primary key not null,
            article_id integer,
            name text,
            total_item_price integer,
            price integer,
            instruction text,
            type text,
            type_id integer,
            item_discount integer,
            cart_discount_rate real,
            cart_discount integer,
            tax_type text
    )""")
    c.execute(
        """CREATE TABLE IF NOT EXISTS Restaurant(
            id INTEGER PRIMARY KEY not null,
            resto_id integer,
            nom text,
            phone text,
            pays text,
            ville text,
            adresse text,
            latitude real,
            longitude real,
            restaurant_token text,
            restaurant_zipcode text)""")
    c.execute("""CREATE TABLE IF NOT EXISTS Client(
            id integer primary key not null,
            client_id integer,
            first_name text,
            last_name text,
            email text not null,
            phone text not null,
            adresse text,
            nombre_commande integer) """)
    c.execute("""CREATE TABLE IF NOT EXISTS Commande(
            id integer primary key not null,
            client_id integer,
            restaurant_id integer,
            prix_total integer,
            nombre_article integer,
            type text,
            status text,
            source text,
            accepted_at text,
            fulfill_at text,
            instructions text,
            tax_value real,
            currency text,
            payment text,
            FOREIGN KEY (restaurant_id)
            REFERENCES Restaurant (restaurant_id)
            FOREIGN KEY (client_id)
            REFERENCES Client (client_id)
    ) """)
    c.execute("""CREATE TABLE IF NOT EXISTS article_commande(
            id integer primary key not null,
            article_id integer,
            commande_id integer,
            quantite integer,
            prix_unitaire integer,
            FOREIGN KEY (article_id)
            REFERENCES Article (article_id)
            FOREIGN KEY (commande_id)
            REFERENCES Commande (commande_id)
    ) """)
    c.execute("""CREATE TABLE IF NOT EXISTS options_article(
            id integer primary key not null,
            article_id integer,
            option_id integer,
            quantite integer,
            FOREIGN KEY (article_id)
            REFERENCES Article (article_id)
            FOREIGN KEY (option_id)
            REFERENCES Options (option_id)
    )""")
