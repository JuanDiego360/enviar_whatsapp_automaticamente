import pywhatkit
import contactos
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from datetime import datetime

# Verificar si el diccionario de contactos está vacío
if not contactos.numero_de_contactos():
    print("El diccionario de contactos está vacío. Por favor, ingresa algunos contactos en contactos.py para comenzar.")
    exit()


# Verificar si todos los números comienzan con '+' y si las llaves no están vacías y si los números tienen 13 caracteres
for nombre, numero in contactos.numero_de_contactos().items():
    if not numero.startswith("+"):
        print(f"El número de contacto para '{nombre}' no comienza con '+'. Corrige esto para continuar.")
        exit()
    if numero[:3]=="+57":
        if not len(numero)==13:
            print(f"El número de contacto para '{nombre}' no tiene los 10 números que caracterisa a un número de colombia. Corrige esto para continuar.")
            exit()
    if not nombre:
        print("Hay un nombre de contacto vacío. Corrige esto para continuar.")
        exit()

# Obtener los nombres de los contactos para el autocompletado
contact_names = list(contactos.numero_de_contactos().keys())

# Configurar el autocompletador
contact_completer = WordCompleter(contact_names, ignore_case=True)

# Solicitar el nombre del contacto con autocompletado
nombre = prompt("Ingresa el nombre del contacto: ", completer=contact_completer)

mensaje=input("ingresa el mensaje: ")
opc="t"
while opc!="y" and opc!="n":
    opc=input("quieres enviarlo ahora? y/n: ")
    if opc!="y" and opc!="n":
        print("opcion no valida")
print()
print("*"*len("* cuando se termine el envio te avisaremos con un archivo llamado PyWhatKit_DB.txt *")+2)
print("* cuando se termine el envio te avisaremos con un archivo llamado PyWhatKit_DB.txt *")
print("*"*len("* cuando se termine el envio te avisaremos con un archivo llamado PyWhatKit_DB.txt *")+2)
print()

if opc=="y":

    # Obtener la hora y el minuto actual
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    pywhatkit.sendwhatmsg(contactos.numero_de_contactos()[nombre], mensaje, current_hour, current_minute + 1, 15, False, 2)
elif opc=="n":
    hora=input("ingresa la hora: ")
    minuto=input("ingresa el minuto: ")
    pywhatkit.sendwhatmsg(contactos.numero_de_contactos()[nombre], mensaje, int(hora), int(minuto), 15, True, 2)