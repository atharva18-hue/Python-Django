import pymysql
from pymongo import MongoClient

class MarvelFilmOperations:
    def __init__(self):
        self.mysql_config = {
            "host": "mysql-atharva-atharvachavhan18-mysql.h.aivencloud.com",
            "port": 28549,
            "user": "avnadmin",
            "password": "AVNS_jFmx0kV_GRKZGe5pdXP",
            "database": "AtharvaDB",
            "ssl": {"ssl": {"ssl": True}}  # Required for Aiven SSL connection
        }

    def allmarvelmoviesinsequence(self):
        con = pymysql.connect(**self.mysql_config)
        curs = con.cursor()
        curs.execute("SELECT * FROM movie_sequence")
        data = curs.fetchall()
        print(data)
        con.close()
        return data

    def addsuperhero(self, hero_name, real_name, title, origin_story, species, superpowers, weakness, gadgets, team, description):
        con = pymysql.connect(**self.mysql_config)
        curs = con.cursor()
        curs.execute("""
            INSERT INTO superheroes (hero_name, real_name, title, origin_story, species, superpowers, weakness, gadgets, team, description)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (hero_name, real_name, title, origin_story, species, superpowers, weakness, gadgets, team, description))
        con.commit()
        con.close()
        return "Superhero added successfully"

    def displaysuperhero(self, hero_name):
        con = pymysql.connect(**self.mysql_config)
        curs = con.cursor()
        curs.execute("SELECT * FROM superheroes WHERE hero_name = %s", (hero_name,))
        data = curs.fetchone()
        con.close()
        if data:
            superhero = {
                "id": data[0],
                "name": data[1],
                "real_name": data[2],
                "title": data[3],
                "origin": data[4],
                "species": data[5],
                "powers": data[6],
                "weakness": data[7],
                "gadgets": data[8],
                "team": data[9],
                "description": data[10],
                "image_url": data[11] if len(data) > 11 else None
            }
            print(superhero)
            return superhero
        else:
            return None

    def submitfanstory(self, title, author, content):
        con = pymysql.connect(**self.mysql_config)
        curs = con.cursor()
        curs.execute("""
            INSERT INTO fan_stories (title, author, content)
            VALUES (%s, %s, %s)
        """, (title, author, content))
        con.commit()
        con.close()
        return "Fan story added successfully"

   

    def upcomeingmarvelmovies(self):
        con = pymysql.connect(**self.mysql_config)
        curs = con.cursor()
        curs.execute("SELECT * FROM Upcoming_Marvel_Movies")
        data = curs.fetchall()
        print(data)
        con.close()
        return data
