import sqlite3

def conectar():
    con = sqlite3.connect('agenda.db')
    cursor = con.cursor()
    return con, cursor

def crear_tabla():
    con, cursor = conectar()
    cursor.execute('CREATE TABLE IF NOT EXISTS contactos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, telefono TEXT)')
    con.commit()
    con.close()

def agregar_contacto():
    con, cursor = conectar()
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el teléfono del contacto: ")
    cursor.execute("INSERT INTO contactos (nombre, telefono) VALUES (?, ?)", (nombre, telefono))
    con.commit()
    con.close()

def listar_contactos():
    con, cursor = conectar()
    cursor.execute("SELECT * FROM contactos")
    for fila in cursor.fetchall():
        print(f"ID: {fila[0]}, Nombre: {fila[1]}, Teléfono: {fila[2]}")
    con.close()

def modificar_contacto():
    con, cursor = conectar()
    listar_contactos()
    id_contacto = int(input("Ingresa el ID del contacto a modificar: "))
    nuevo_nombre = input("Ingresa el nuevo nombre: ")
    nuevo_telefono = input("Ingresa el nuevo teléfono: ")
    cursor.execute("UPDATE contactos SET nombre = ?, telefono = ? WHERE id = ?", (nuevo_nombre, nuevo_telefono, id_contacto))
    con.commit()
    con.close()

def eliminar_contacto():
    con, cursor = conectar()
    listar_contactos()
    id_contacto = int(input("Ingresa el ID del contacto a eliminar: "))
    cursor.execute("DELETE FROM contactos WHERE id = ?", (id_contacto,))
    con.commit()
    con.close()

def main():
    crear_tabla()
    while True:
        print("----- Agenda -----")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Modificar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            listar_contactos()
        elif opcion == '3':
            modificar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            break
        else:
            print("Opción no válida")

if __name__ == '__main__':
    main()
