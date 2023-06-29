import psycopg2

def drop_table(cursor):
    cursor.execute("""
             DROP TABLE phones;
             DROP TABLE clients;
             """)
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
                ON DELETE CASCADE
            );
        """
    cursor.execute(create_clients)
    cursor.execute(create_phones)
    return print("Tables were created successfully")

def add_client(cursor, first_name, surname, e_mail):
    insert_client = 'INSERT INTO clients(first_name, surname, e_mail) VALUES (%s, %s, %s) returning id, first_name, surname, e_mail'
    client_data = (first_name, surname, e_mail)
    cursor.execute(insert_client, client_data)
    return print('The data on a client were inserted successfully', cursor.fetchall())

def add_phone(cursor, number, client_id):
    insert_phone = "INSERT INTO phones(number, client_id) VALUES (%s, %s) returning id, number, client_id"
    phone_data = number, client_id
    cursor.execute(insert_phone, phone_data)
    return print('The phone number was added successfully', cursor.fetchall())

def update_client(cursor, id, first_name, surname, e_mail,number):
    if first_name:
        update_data = "UPDATE clients SET first_name=%s WHERE id=%s returning id, first_name, surname, e_mail"
        client_data = (first_name, id)
        cursor.execute(update_data, client_data)
        print("The data were changed successfully", cursor.fetchall())
    if surname:
        update_data = "UPDATE clients SET surname=%s WHERE id=%s returning id, first_name, surname, e_mail"
        client_data = (surname, id)
        cursor.execute(update_data, client_data)
        print("The data were changed successfully", cursor.fetchall())
    if e_mail:
        update_data = "UPDATE clients SET e_mail=%s WHERE id=%s returning id, first_name, surname, e_mail"
        client_data = (e_mail, id)
        cursor.execute(update_data, client_data)
        print("The data were changed successfully", cursor.fetchall())
    if number:
        update_data = "UPDATE phones SET number=%s WHERE id=%s returning id, number"
        client_data = (number, id)
        cursor.execute(update_data, client_data)
        print("The data were changed successfully", cursor.fetchall())
        return

def search_client(cursor, first_name, surname, e_mail, number):
    if first_name:
        cursor.execute(
            """SELECT c.id, c.first_name, c.surname, c.e_mail, ph.number FROM clients c
            JOIN phones ph on ph.client_id = c.id
            WHERE c.first_name LIKE %s;""", (first_name,))
    if surname:
        cursor.execute(
            """SELECT c.id, c.first_name, c.surname, c.e_mail, ph.number FROM clients c
            JOIN phones ph on ph.client_id = c.id
            WHERE c.surname LIKE %s;""", (surname,))
    if e_mail:
        cursor.execute(
            """SELECT c.id, c.first_name, c.surname, c.e_mail, ph.number FROM clients c
            JOIN phones ph on ph.client_id = c.id
            WHERE c.e_mail LIKE %s;""", (e_mail,))
    if number:
        cursor.execute(
            """SELECT c.id, c.first_name, c.surname, c.e_mail, ph.number FROM clients c
            JOIN phones ph on ph.client_id = c.id
            WHERE ph.number LIKE %s;""", (number,))

    result = cursor.fetchall()
    if len(result) == 0:
        print('There is no such client in the database')
    else:
        for client in result:
            print(f'The following client was found: {client[0]}, {client[1]}, {client[2]}, {client[3]}, {client[4]}')

def delete_phone(cursor, id):
    delete_number = "DELETE FROM phones where id=%s"
    phone_data = (id,)
    cursor.execute(delete_number, phone_data)
    return print("The number was deleted")

def delete_client(cursor, id):
    delete_data = "DELETE FROM clients where id=%s"
    client_id = (id,)
    cursor.execute(delete_data, client_id)
    conn.commit()
    return print("The data on a client were deleted")

with psycopg2.connect(database="clients_phones", user="postgres", password="psgegel") as conn:
    cursor = conn.cursor()
    if __name__ == "__main__":
        drop_table(cursor)
        create_table(cursor)

        add_client(cursor,"Jean-Luc", "Picard", "jl.picard@starfleet.org")
        add_client(cursor, 'Kathryn', 'Janeway', "k.janeway@starfleet.org")
        add_client(cursor, 'Annika', 'Janeway', "a.janeway@starfleet.org")

        add_phone(cursor, "1234", 1)
        add_phone(cursor, '2345', 2)
        add_phone(cursor, '3456', 3)

        number = None
        first_name = None
        e_mail = None
        surname = None
        update_client(cursor, 1, first_name, "Godard", "jl.godard@gmail.com", number)

        search_client(cursor, first_name, "Janeway", e_mail, number)

        delete_phone(cursor, 3)

        delete_client(cursor, 1)

conn.close()
