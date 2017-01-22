"""Postgres database interaction
Copyright 2017, Sjors van Gelderen
"""

import psycopg2


# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    #try:
    #   connect("host='128.199.52.191', user='euromast', password='groep6', dbname='euromast'")
    #except: print("Ik kon geen verbinding maken met de database :(")
    # Tabelnaam ^ == "scores"
    # Bij het inserted de id meegeven :P
    connection = psycopg2.connect(dbname="mydb", user="postgres", password="admin")
    cursor = connection.cursor()
    
    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()
    
    return results

def insert_player(name, score):
    return interact_with_database("INSERT INTO score (name, playerscore) VALUES ('{}', {});".format(name, score))

insert_player("Rickvb10", 500)

# Uploads a score into the hiscore table
def upload_score(name, score):
    interact_with_database("UPDATE score SET playerscore = {} WHERE name = '{}'"
                           .format(score, name))


# Downloads score data from database
def download_scores():
    return interact_with_database("SELECT * FROM score")


# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM score ORDER BY playerscore")[0][1]
    return result
