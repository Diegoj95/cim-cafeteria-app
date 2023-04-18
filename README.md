# cim-cafeteria-app

## Contenidos
- [Aplicación cafetería](#cim-cafeteria-app)
  - [Contenidos](#contenidos)
  - [Breve Descripción](#Breve-Descripción)
    - [¿Cuál es el problema?](#¿Cuál-es-el-problema?)
    - [¿Cómo puede ayudar la tecnología?](#¿Cómo-puede-ayudar-la-tecnología?)
  - [Construido con](#Construido-con)
  - [Instalación y recomendaciones para continuación del proyecto](#Instalación-y-recomendaciones-para-continuación-del-proyecto)
  - [Repositorio separado](#Repositorio-separado)
  - [Autores](#Autores)
    

## Breve descripción

Este prototipo fue desarrollado como tarea durante práctica profesional en el CIMUBB de la Universidad del Bío-Bío. Consiste en mostrar datos recopilados por una aplicación que utiliza reconocimiento de imágenes. 
### ¿Cuál es el problema?

Estudiantes, funcionarios o docentes en la Universidad necesitan saber la disponibilidad de mesas libres en el casino de la Universidad para poder ir a comer tranquilamente.


### ¿Cómo puede ayudar la tecnología?

Con la aplicación los usuarios pueden obtener acceso a la información proporcionada por los datos recopilados.


## Imágenes de la aplicación
![a](https://i.imgur.com/JsKCOlL.jpg)


## Construido con

- Python 3.10.10
- Kivy 2.1.0
- Buildozer
- Google Sheets

## Instalación y recomendaciones para continuación del proyecto

1. Instalar una versión de python compatible con la versión de kivy a utilizar, en este caso se utilizó la versión de [python 3.10.10](https://www.python.org/downloads/release/python-31010/) y [kivy 2.1.0](https://kivy.org/doc/stable/gettingstarted/installation.html)
2. Para generar una apk de android se requiere un ambiente Linux, en teoria se puede generar la apk con un subsistema de Linux para Windows pero es preferible utilizar una máquina virtual para evitar errores
3. Instalar buildozer en Linux, se recomienda leer la [documentación](https://buildozer.readthedocs.io/en/latest/installation.html) y ver el siguiente [vídeo](https://www.youtube.com/watch?v=pzsvN3fuBA0&ab_channel=DENICZ)
4. Al generar la apk se deben tener instaladas en Linux todas las librerias utilizadas y declarandolas en el apartado "requeriments" del archivo buildozer.spec

5. Ejemplo de como instalar los requerimientos actuales del proyecto en la consola de Linux
```python
pip install kivy google-auth google-auth-oauthlib httplib2 pyasn1 pyasn1-modules rsa oauth2client requests gspread cachetools urllib3 chardet charset_normalizer idna requests_oauthlib oauthlib pyparsing
```
6. Conectar google sheets con python, [vídeo](https://www.youtube.com/watch?v=lI98OTpKarY&ab_channel=ArtificialCorner)

## Repositorio separado

* [Procesamiento de imágenes](https://github.com/Diegoj95/cim-cafeteria-camara)

## Autores

* Diego Jiménez - diego.jimenez1901@alumnos.ubiobio.cl
* Ignacio Pardo - ignacio.pardo1901@alumnos.ubiobio.cl

