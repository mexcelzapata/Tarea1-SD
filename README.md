# Tarea1-SD
Este repositorio tiene como objetivo poder dejar los diferentes archivos que permiten dar respuesta a la tarea N°1. En este caso consta de 3 modulos: Buscador (API-REST), Cache y inventario.




## Buscador (API - REST)
Este modulo consta de la busqueda de una palabra que se quiera buscar en el inventario, para ello, se implementó una busqueda atraves del metodo `HTTP-Request`.
Para ello, tenemos el archivo **"/Buscador/"** el cual contiene el la informacion para levantar el servidor de forma local. Para esta ocacion es necesario instalar `python 3.8.10`
ademas del Framework `Flask`.


### Python 3.8.10
```
sudo apt update
sudo apt install software-properties-common
sudo apt install python3.8.10
```
### Flask

```
pip install flask
```

Una vez instalado, es necesario abrir la terminal y ubicatrnos en el documento **API_client.py** y lo ejecutamos:
```
python3 API_client.py
```
Tenemos que tener presente que una vez instaladas todas las componentes, este buscador está ubicado en : `Localhost:3000\inventory\search?=**BUSCAR**`




## Cache (Reddis)
En este caso, tenemos que 







