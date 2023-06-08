from time import sleep
import pickle
import sys
import os

phonebook = {}

def load_phonebook(book_path):
    book_name = os.path.basename(book_path)

    print(f'Abriendo la agenda [{book_name}] ...')
    sleep(1)
    if not os.path.exists(f'{book_path}.bin'):
        print(f'La agenda [{book_name}] no existe!')
        sleep(2)
        return -1

    if not os.path.getsize(f'{book_path}.bin'):
        print(f'La agenda [{book_name}] está vacía')
        return {}

    try:
        with open(f'{book_path}.bin', 'rb') as fhand:
            book = pickle.load(fhand)
        return book
    except:
        print(f'ERROR: ¡La agenda [{book_name}] existe, pero no se pudo leer!')
        sleep(2)
        return -1


def create_phonebook(book_path):
    book_name = os.path.basename(book_path)

    print(f'Creando la agenda [{book_name}] ...')
    sleep(1)
    if os.path.exists(f'{book_path}.bin') and os.path.getsize(f'{book_path}.bin'):
        print(f'La agenda [{book_name}] existe y tiene datos. Por seguridad, no se creará\n'
              'una agenda nueva que sobreescriba otra existente conteniendo datos.\n'
              'Primero debe borrarla, bien desde el menú principal, o bien manualmente.\n'
              )
        input('Pulse enter para continuar ...')
        return -1

    try:
        fhand = open(f'{book_path}.bin', 'wb')
        fhand.close()
    except:
        print(f'ERROR: ¡No se pudo crear la agenda [{book_name}]!')
        sleep(2)
        return -1

    return {}


def delete_phonebook(book_path):
    book_name = os.path.basename(book_path)

    option = input(f'Está seguro que desea borrar permanentemente la agenda [{book_name}] [y/N]: ')
    if option.lower() == 'y':
        if not os.path.exists(f'{book_path}.bin'):
            print(f'La agenda [{book_name}] NO existe, compruebe el nombre.')
            sleep(2)
            return -1
        try:
            print(f'Borrando la agenda [{book_name}] ...')
            os.remove(f'{book_path}.bin')
            sleep(1)
            print(f'La agenda [{book_name}] fue borrada con éxito.')
            sleep(2)
        except:
            print(f'ERROR: ¡La agenda [{book_name}] existe, pero no se pudo borrar!')
            sleep(2)
            return -1


def save_phonebook(book_path, pbook):
    book_name = os.path.basename(book_path)

    try:
        print(f'Guardando la agenda [{book_name}] ...')
        with open(f'{book_path}.bin', 'wb') as fhand:
            pickle.dump(pbook, fhand)
        sleep(1)
    except:
        print(f'ERROR: ¡La agenda [{book_name}] no se pudo guardar!')
        sleep(2)
        return -1


def phonebook_changed(book_path, pbook):
    book_name = os.path.basename(book_path)

    if not os.path.exists(f'{book_path}.bin'):
        print(f'La agenda [{book_name}] no existe!')
        sleep(2)
        return False

    if not os.path.getsize(f'{book_path}.bin'):
        print(f'La agenda [{book_name}] está vacía')
        return False

    try:
        with open(f'{book_path}.bin', 'rb') as fhand:
            old_book = pickle.load(fhand)
        if old_book != pbook:
            print(f'La agenda [{book_name}] ha sido modificada desde la última vez que se guardó.')
            return True
    except:
        print(f'ERROR: ¡La agenda [{book_name}] existe, pero no se pudo leer!')
        sleep(2)
        return False

    return False


def show_contacts(contact, pbook):
    found = False
    for name, numbers in pbook.items():
        if name.lower().startswith(contact.lower()):
            print(f'{name}: {", ".join(numbers)}')
            found = True

    if not found:
        print(f'No se encontraron contactos que coincidan con "{contact}"')


def add_contact(first, last, numbers, pbook):
    name = f'{first} {last}'
    if name in pbook:
        print(f'El contacto "{name}" ya existe en la agenda.')
        return -1

    pbook[name] = numbers
    print(f'Se agregó el contacto "{name}" a la agenda.')


def show_all_contacts(pbook):
    if not pbook:
        print('La agenda está vacía.')
        return

    for name, numbers in pbook.items():
        print(f'{name}: {", ".join(numbers)}')


def add_phone(contact, phone, pbook):
    if contact not in pbook:
        print(f'El contacto "{contact}" no existe en la agenda.')
        return -1

    pbook[contact].append(phone)
    print(f'Se agregó el número "{phone}" al contacto "{contact}".')


def delete_phone(contact, pbook):
    if contact not in pbook:
        print(f'El contacto "{contact}" no existe en la agenda.')
        return -1

    numbers = pbook[contact]
    if len(numbers) == 1:
        print(f'El contacto "{contact}" solo tiene un número de teléfono. '
              'No se puede borrar el último número.')
        return -1

    print(f'Números de teléfono de "{contact}":')
    for i, phone in enumerate(numbers):
        print(f'{i + 1}. {phone}')

    try:
        option = int(input('Ingrese el número correspondiente al teléfono que desea borrar: '))
        if 1 <= option <= len(numbers):
            del pbook[contact][option - 1]
            print(f'Se borró el número de teléfono del contacto "{contact}".')
        else:
            print('Opción inválida.')
    except ValueError:
        print('Opción inválida. Debe ingresar un número.')
    except:
        print('Ocurrió un error al borrar el número de teléfono.')


def delete_contact(contact, pbook):
    if contact not in pbook:
        print(f'El contacto "{contact}" no existe en la agenda.')
        return -1

    del pbook[contact]
    print(f'Se borró el contacto "{contact}" de la agenda.')


def secondary_menu():
    while True:
        print('\n--- Menú secundario ---')
        print('1. Agregar un número de teléfono a un contacto existente')
        print('2. Borrar un número de teléfono de un contacto')
        print('3. Borrar un contacto')
        print('0. Volver al menú principal')

        try:
            option = int(input('Seleccione una opción: '))
            if option == 1:
                contact = input('Ingrese el nombre del contacto: ')
                phone = input('Ingrese el número de teléfono: ')
                add_phone(contact, phone, phonebook)
            elif option == 2:
                contact = input('Ingrese el nombre del contacto: ')
                delete_phone(contact, phonebook)
            elif option == 3:
                contact = input('Ingrese el nombre del contacto: ')
                delete_contact(contact, phonebook)
            elif option == 0:
                return
            else:
                print('Opción inválida.')
        except ValueError:
            print('Opción inválida. Debe ingresar un número.')
        except:
            print('Ocurrió un error al ejecutar la opción.')
