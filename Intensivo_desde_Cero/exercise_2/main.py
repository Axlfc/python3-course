from phonebook_functions import *

WORKDIR = f'{os.environ["HOME"]}/.phonebook'
BOOKS = f'{WORKDIR}/books'

phonebook_name = 'phonebook'

def main_menu():
    while True:
        print('\n--- Menú principal ---')
        print('1. Mostrar todos los contactos')
        print('2. Buscar contactos por nombre')
        print('3. Agregar un nuevo contacto')
        print('4. Borrar la agenda actual')
        print('9. Guardar y salir')
        print('0. Salir sin guardar')

        try:
            option = int(input('Seleccione una opción: '))
            if option == 1:
                show_all_contacts(phonebook)
            elif option == 2:
                contact = input('Ingrese el nombre o las primeras letras del nombre del contacto: ')
                show_contacts(contact, phonebook)
            elif option == 3:
                first = input('Ingrese el primer nombre: ')
                last = input('Ingrese el apellido: ')
                numbers = input('Ingrese los números de teléfono separados por comas: ').split(',')
                add_contact(first, last, numbers, phonebook)
            elif option == 4:
                delete_phonebook(f'{BOOKS}/{phonebook_name}')
                return -1
            elif option == 9:
                if phonebook_changed(f'{BOOKS}/{phonebook_name}', phonebook):
                    option = input('La agenda ha sido modificada. ¿Desea guardar los cambios? [y/N]: ')
                    if option.lower() == 'y':
                        save_phonebook(f'{BOOKS}/{phonebook_name}', phonebook)
                        print('La agenda se guardó exitosamente.')
                        return -1
                else:
                    print('La agenda no ha sido modificada.')
                    return -1
            elif option == 0:
                option = input('¿Está seguro que desea salir sin guardar? [y/N]: ')
                if option.lower() == 'y':
                    return -1
            else:
                print('Opción inválida.')
        except ValueError:
            print('Opción inválida. Debe ingresar un número.')
        except:
            print('Ocurrió un error al ejecutar la opción.')

def main():

    print('--- Gestor de Agenda ---')

    if not os.path.exists(WORKDIR):
        os.makedirs(WORKDIR)

    if not os.path.exists(BOOKS):
        os.makedirs(BOOKS)

    book_path = f'{BOOKS}/{phonebook_name}'

    if not load_phonebook(book_path):
        create_phonebook(book_path)

    while True:
        if main_menu() == -1:
            break

    print('¡Hasta pronto!')


if __name__ == '__main__':
    main()
