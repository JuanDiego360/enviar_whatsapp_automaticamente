# Proyecto de Envío de Mensajes con PyWhatKit

Este proyecto utiliza la biblioteca PyWhatKit para enviar mensajes de WhatsApp automáticamente desde Python. Los contactos se gestionan en un archivo separado y se proporciona autocompletado para facilitar la selección de contactos.

## Características

- Envío automático de mensajes de WhatsApp.
- Autocompletado de nombres de contacto.
- Configuración flexible de hora de envío.
- Validación de contactos: El script verifica que todos los números de teléfono comiencen con "+" y que los nombres de los contactos no estén vacíos para evitar errores en el envío de mensajes.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/JuanDiego360/enviar_whatsapp_automaticamente.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd enviar_whatsapp_automaticamente
   ```

3. Crea un entorno virtual:

   ```bash
   python3 -m venv .venv
   ```

4. Activa el entorno virtual:

   - En Linux/Mac:

     ```bash
     source .venv/bin/activate
     ```

   - En Windows:

     ```bash
     .venv\\Scripts\\activate
     ```

5. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Asegúrate de que el archivo `contactos.py` tenga los contactos necesarios.
2. Ejecuta el script principal:

   ```bash
   python enviar_mensajes.py
   ```

3. Sigue las instrucciones en pantalla para enviar un mensaje.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, envía un pull request para mejoras.