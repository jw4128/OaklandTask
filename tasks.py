import requests
import sys
import sqlite3

### TASK 1 ###

clefairyData = requests.get("https://pokeapi.co/api/v2/pokemon/clefairy").json()
print(clefairyData)

### TASK 2 ###

clefairyDictionary = {
    "ID" : clefairyData["id"],
    "Name" : clefairyData["name"],
    "Height" : clefairyData["height"],
    "Weight" : clefairyData["weight"]
}

print(clefairyDictionary)


### TASK 3 ###

def returnDictionary(name):
    pokemonData = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").json()

    pokemonDictionary = {
        "ID" : pokemonData["id"],
        "Name" : pokemonData["name"],
        "Height" : pokemonData["height"],
        "Weight" : pokemonData["weight"]
    }

    return pokemonDictionary

print(returnDictionary("PikAchu"))

"""
### TASK 4 ###

name = sys.argv[1]

print(returnDictionary(name))
"""
### TASK 5 ###
def print_info(info):
    #print(info)
    if type(info) == tuple:
        print("### POKEMON INFO ###")
        print(f"ID:      | {info[0]}\nName:    | {info[1]}\nHeight:  | {info[2]}\nWeight:  | {info[3]}\n")
    else:
        print(info)

def add_pokemon(con, name):
    sql = '''INSERT INTO pokemon(id, name, height, weight) VALUES(?,?,?,?)'''
    cur = con.cursor()
    try:
        pokemonData = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").json()
    except:
        return "Pokemon not found, please check spelling"
    databaseValues = [pokemonData["id"], pokemonData["name"], pokemonData["height"], pokemonData["weight"]]
    cur.execute(sql, databaseValues)
    con.commit()
    return tuple(databaseValues)

def get_pokemon_info(con, name):
    print("in call")
    name = name.lower()
    try:
        print("in try")
        cur = con.cursor()
        cur.execute("SELECT id, name, height, weight FROM pokemon WHERE name =?", (name,))
        row = cur.fetchone()
        if row:
            print("found!")
            print_info(row)
        else:
            print("not found. adding...")
            print_info(add_pokemon(con, name))
    except sqlite3.OperationalError:
        print("Error")


con = sqlite3.connect("poke.db")    #create connection to database "poke"
cur = con.cursor()  #create cursor to execute SQL statements and fetch results from queries
cur.execute("CREATE TABLE IF NOT EXISTS pokemon(id, name, height, weight)")   #create table in database if it doesn't already exist
print("before call")
get_pokemon_info(con, "milotic")
print("after call")
con.close() #need to close the connection when you're finished

