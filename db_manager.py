import psycopg2


class HeroDatabase:
    """Simple PostgreSQL handler for hero records."""

    def __init__(self):
        """Initialize database connection and cursor."""
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                database="rpg_db",
                user="postgres",
                password="YOUR_PASSWORD_HERE",
                port="5432",
            )
            self.cursor = self.connection.cursor()
            print("🔌 Database connected successfully!")

        except Exception as error:
            print(f"Error while trying to connect: {error}")

    def add_hero(self, name, role, level, gold, is_alive):
        """Insert a new hero into the database."""
        query = """
        INSERT INTO heroes (name, role, level, gold_coins, is_alive)
        VALUES (%s, %s, %s, %s, %s);
        """
        data = (name, role, level, gold, is_alive)

        self.cursor.execute(query, data)
        self.connection.commit()

        print(f"✅ Hero '{name}' added to the database!")

    def get_heroes(self):
        """Return all heroes ordered by ID."""
        query = "SELECT * FROM heroes ORDER BY id ASC;"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def update_hero(self, hero_id, new_level, new_gold):
        """
        Updates the level and gold of a specific hero identified by their ID.
        """

        query = """ 
        UPDATE heroes
        SET level = %s, gold_coins = %s
        WHERE id = %s;
        """

        data = (new_level, new_gold, hero_id)

        try:
            self.cursor.execute(query, data)
            self.connection.commit()

            if self.cursor.rowcount > 0:
                print(f"✅ Hero (ID {hero_id}) updated successfully!")
            else:
                print(f"⚠️ Hero (ID {hero_id}) not found.")

        except Exception as e:
            print(f"Falied to update hero: {e}")

    def delete_hero(self, hero_id):
        """
        Permanently removes a hero from the database.
        Warning: This action cannot be undone.
        """

        query = "DELETE FROM heroes WHERE id = %s;"

        data = (hero_id,)

        try:
            self.cursor.execute(query, data)
            self.connection.commit()

            if self.cursor.rowcount > 0:
                print(f"❌ Hero (ID {hero_id}) deleted successfully!")
            else:
                print(f"⚠️ Hero (ID {hero_id}) not found.")

        except Exception as e:
            print(f"Failed to delete hero: {e}")

        

    def close_connection(self):
        """Safely close cursor and database connection."""
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()

        print("🚪 Connection closed.")


if __name__ == "__main__":
    db = HeroDatabase()

    print("--- Creating Test Dummy ---")
    db.add_hero("Test Dummy", "None", 1, 0, False)

    all_heroes = db.get_heroes()
    last_hero = all_heroes[-1]
    id_to_delete = last_hero[0]

    print(f"Target identified: {last_hero[1]} with ID {id_to_delete}")

    print(f"\n🗑️ DELETING ID {id_to_delete}...")
    db.delete_hero(id_to_delete)

    print("\n📋 Final Guild List:")
    final_list = db.get_heroes()
    for hero in final_list:
        print(hero)

    db.close_connection()