import pandas as pd


def convertir_excel_a_csv(excel_file, csv_file):
    try:
        df = pd.read_excel(excel_file)
        df.to_csv(csv_file, index=False)
        print("Archivo CSV generado correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo de Excel.")
    except Exception as e:
        print("Error al convertir el archivo de Excel a CSV:", e)


def main():
    excel_file = input('Dime un archivo de excel (.xlsx): ')
    csv_file = f"{excel_file.split('.')[0]}.csv"

    convertir_excel_a_csv(excel_file, csv_file)


if __name__ == '__main__':
    main()
