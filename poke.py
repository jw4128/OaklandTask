import requests
import sys
import sqlite3

# Function to print the information in a nice way
def print_info(info):
    if type(info) == tuple:
        print("### POKEMON INFO ###")
        print(f"ID:      | {info[0]}\nName:    | {info[1]}\nHeight:  | {info[2]}\nWeight:  | {info[3]}\n")
    else:
        print(info)

# Function to add information to database
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

# Function to get the information for a pokemon
def get_pokemon_info(con, name):
    name = name.lower()
    try:
        cur = con.cursor()
        cur.execute("SELECT id, name, height, weight FROM pokemon WHERE name =?", (name,))
        row = cur.fetchone()
        if row:
            print("Found in database!")
            print_info(row)
        else:
            print("Not found. Adding to database...")
            print_info(add_pokemon(con, name))
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Setting up the database and table
    con = sqlite3.connect("poke.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS pokemon(id, name, height, weight)")

    # Run from the command line
    if len(sys.argv) > 1:
        name = "-".join(sys.argv[1:]).strip()
    else:
        name = input("Enter a Pokemon name: ").strip()
        
    get_pokemon_info(con, name)
    con.close()


if __name__ == "__main__":
    main()