import sqlite3
from sqlite3 import Error

# Create database and insert
conn = sqlite3.connect('restorapid_db.db')
c = conn.cursor()


class Restaurant:
    def __init__(self, resto_id, nom, phone, pays, ville, adresse, latitude, longitude, restaurant_token, restaurant_zipcode):
        self.resto_id = resto_id
        self.nom = nom
        self.phone = phone
        self.pays = pays
        self.ville = ville
        self.adresse = adresse
        self.latitude = latitude
        self.longitude = longitude
        self.restaurant_token = restaurant_token
        self.restaurant_zipcode = restaurant_zipcode

    def insertion(self):
        c.execute("INSERT INTO Restaurant(resto_id,nom,phone,pays,ville,adresse,latitude,longitude,restaurant_token,restaurant_zipcode) VALUES(?,?,?,?,?,?,?,?,?,?)",
                  (self.resto_id, self.nom, self.phone, self.pays, self.ville, self.adresse, self.latitude, self.longitude, self.restaurant_token, self.restaurant_zipcode))
        conn.commit()
        c.close()
        conn.close()
        print('insertion reussi')

    def insertData(self):
        try:
            c.execute("SELECT * FROM Restaurant")
            rows = c.fetchall()
            if not rows:
                self.insertion()
            else:
                for row in rows:
                    if row[1] == self.resto_id:
                        print('resto existe')
                    else:
                        self.insertion()
        except Error as a:
            print(a)


class Client:
    def __init__(self, client_id, first_name, last_name, email, phone, adresse):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.adresse = adresse
        #self.nombre_commande = nombre_commande

    def insertion(self, nombre_commande):
        c.execute("INSERT INTO Client(client_id, first_name, last_name, email, phone, adresse,nombre_commande) VALUES(?,?,?,?,?,?,?)",
                  (self.client_id, self.first_name, self.last_name, self.email, self.phone, self.adresse, nombre_commande))
        conn.commit()
        c.close()
        conn.close()
        print ('insertion reussi')

    def update_client(self, client):
        sql = ''' UPDATE Client SET nombre_commande = ?  WHERE id = ?'''
        c.execute(sql, client)
        conn.commit()
        c.close()
        conn.close()
        print ('update reussi')

    @staticmethod
    def update_client_final(client):
        sql = ''' UPDATE Client SET nombre_commande = ?  WHERE id = ?'''
        c.execute(sql, client)
        conn.commit()
        c.close()
        conn.close()
        print ('update reussi')

    def insertData(self):
        nombre_commande = 0
        c.execute("SELECT * FROM Client")
        rows = c.fetchall()
        if not rows:
            nombre_commande = nombre_commande + 1
            self.insertion(nombre_commande)
        else:
            for row in rows:
                print (row[7])
                if row[1] == self.client_id:
                    if row[7] < 4:
                        self.update_client((row[7] + 1, row[0]))
                    elif row[7] == 4:
                        print("Vous avez gagne")
                        self.update_client((row[7] - 3, row[0]))
                else:
                    nombre_commande = nombre_commande + 1
                    self.insertion(nombre_commande)
