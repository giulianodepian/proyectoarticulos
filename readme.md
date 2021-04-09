### Proyecto Articulos
# Como deployar el proyecto
Paso 1: clonar o descargar repositorio  
Paso 2: crear y meterse en un entorno virtual mediante el comando virtualenv "nombre del entorno virutual" ("pip install virtualenv" en caso de que no se tenga instalado)  
Paso 3: Instalar requerimientos necesarios mediante el comando "pip install -r requirements.txt" dentro de la carpeta clonada  
Paso 4: Modificar en el archivo proyectoarticulos/settings.py la parte de DATABASE con los datos de la base de datos local  
Paso 5: Realizar las migraciones a la base de datos mediante los comando "python manage.py makemigrations" y "python manage.py migrate"  
paso 6: crear un superuser mediante el comando "manage.py createsuperuser" y seguir las instrucciones indicadas  
Paso 7: Correr aplicacion mediante el comando "python manage.py runserver"  
Paso 8: En el navegador ingresar a la direccion localhost:8000  
# Informacion del proyecto
El proyecto consiste en articulos que los usuarios pueden ver, crear y modificar, mientras que solo los admines pueden borrarlos. Tiene un Login y un Logout asi como tambien se puede crear un nuevo usuario.  
Los usuario no logueados solo pueden ver articulos.  
No se tiene estilos css, es una aplicacion simple para mostrar manejo de framework y las funcionalidades de la aplicacion. Los usuarios pueden editar articulos aunque no sean suyos.  