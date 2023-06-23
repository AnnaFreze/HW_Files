import psycopg2

with psycopg2.connect(database="clients_phones", user="postgres", password="psgegel") as conn:
    cursor = conn.cursor()

    def drop_table(cursor):
        cursor.execute("""
                 DROP TABLE phones;
                 DROP TABLE clients;
                 """)
        conn.commit()
        return print("Previous tables were dropped")


    def create_table(cursor):
        create_clients = """
                CREATE TABLE IF NOT EXISTS clients(
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(30) NOT NULL,
                    surname VARCHAR(40) NOT NULL,
                    e_mail  VARCHAR(40) NOT NULL
                    );
                """
        create_phones = """
                CREATE TABLE IF NOT EXISTS phones(
                    id SERIAL PRIMARY KEY,
                    number VARCHAR (15) NOT NULL,
                    client_id INTEGER NOT NULL REFERENCES clients(id)
                );
            """
        cursor.execute(create_clients)
        cursor.execute(create_phones)
        conn.commit()
        return print("Tables were created successfully")

    def add_client(cursor, first_name, surname, e_mail):
        insert_client = 'INSERT INTO clients(first_name, surname, e_mail) VALUES (%s, %s, %s) returning id, first_name, surname, e_mail'
        client_data = (first_name, surname, e_mail)
        cursor.execute(insert_client, client_data)
        conn.commit()
        return print('The data on a client were inserted successfully', cursor.fetchall())

    def add_phone(cursor, number, client_id):
        insert_phone = "INSERT INTO phones(number, client_id) VALUES (%s, %s) returning id, number, client_id"
        phone_data = number, client_id
        cursor.execute(insert_phone, phone_data)
        conn.commit()
        return print('The phone number was added successfully', cursor.fetchall())

    def update_client(cursor, id, first_name, surname, e_mail):
        update_data = "UPDATE clients SET first_name=%s, surname=%s, e_mail=%s WHERE id=%s returning id, first_name, surname, e_mail"
        client_data = (first_name, surname, e_mail, id)
        cursor.execute(update_data, client_data)
        conn.commit()
        return print("The data were changed successfully", cursor.fetchall())

    def search_client(cursor,first_name, surname, e_mail,number):
        search_data = "SELECT c.id, c.first_name, c.surname, c.e_mail, ph.number FROM clients c JOIN phones ph on ph.client_id = c.id WHERE c.first_name LIKE %s or c.surname LIKE %s or c.e_mail LIKE %s or ph.number LIKE %s"
        client_data = (first_name, surname, e_mail, number)
        cursor.execute(search_data, client_data)
        conn.commit()
        return print("The client is found", cursor.fetchall())

    def delete_phone(cursor, id):
        delete_number = "DELETE FROM phones where id=%s"
        phone_data = (id,)
        cursor.execute(delete_number, phone_data)
        conn.commit()
        return print("The number was deleted")

    def delete_client(cursor, id):
        delete_data = "DELETE FROM clients where id=%s"
        client_id = (id,)
        cursor.execute(delete_data, client_id)
        conn.commit()
        return print("The data on a client were deleted")

    if __name__ == "__main__":
        drop_table(cursor)
        create_table(cursor)

        first_name = "Jean-Luc"
        surname = "Picard"
        e_mail = "jp.picard@starfleet.org"
        add_client(cursor,first_name, surname, e_mail)

        number = "1234"
        client_id = 1
        add_phone(cursor, number, client_id)

        id = 1
        surname = "Godard"
        e_mail = "jp.godard@gmail.com"
        update_client(cursor, id, first_name, surname, e_mail)

        search_client(cursor, first_name, surname, e_mail, number)

        delete_phone(cursor, id)

        delete_client(cursor, id)

conn.close()