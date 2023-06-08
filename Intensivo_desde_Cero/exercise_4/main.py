import requests
from dotenv import load_dotenv
import os


def obtener_informacion_climatica(ciudad, codigo_pais, api_key, lang):
    try:
        city_name = ciudad.strip().lower().replace(' ', '%20')
        country_code = codigo_pais.strip().lower().replace(' ', '%20')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&lang={lang}'

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print("Error al obtener la información climática:", response.json()["message"])
            return None
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud:", e)
        return None
    except KeyError:
        print("Error al procesar los datos de la respuesta.")
        return None


def main():
    load_dotenv()
    api_key = os.environ["OPENWEATHERMAP_API_KEY"]

    ciudad = input("Ingresa el nombre de la ciudad: ")
    codigo_pais = input("Ingresa el código del país (por ejemplo, 'es' para España): ")
    informacion_climatica = obtener_informacion_climatica(ciudad, codigo_pais, api_key, 'es')

    if informacion_climatica:
        main = informacion_climatica['main']
        temp = round(main['temp'] - 273.15, 1)
        max_temp = round(main['temp_max'] - 273.15, 1)
        min_temp = round(main['temp_min'] - 273.15, 1)
        feels_like = round(main['feels_like'] - 273.15, 1)
        pressure = main['pressure']
        humidity = main['humidity']

        print()
        print(f'  Ciudad: {informacion_climatica["name"]}')
        print()
        print(f'    Temperatura:          {temp}°C')
        print(f'    Temperatura máxima:   {max_temp}°C')
        print(f'    Temperatura mínima:   {min_temp}°C')
        print(f'    Sensación térmica:    {feels_like}°C')
        print(f'    Presión atmosférica:  {pressure} hPa')
        print(f'    Humedad relativa:     {humidity}%')
        print()


if __name__ == '__main__':
    main()
