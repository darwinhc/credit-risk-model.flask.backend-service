# API para el uso de modelo para generar un indicador de riesgo crediticio con respecto a una persona

Se desarrolla un modelo de un scoreboard para el riesgo crediticio que trae consigo una persona

## Uso 

Use la API realizando peticiones POST a la siguiente ruta
~~~
https://modelo-riesgo-crediticio.herokuapp.com/
~~~

Enviando los datos requeridos de la siguiente manera

~~~json
{
  "sub_grade": "string", 
  "int_rate": "float", 
  "out_prncp": "float"
}
~~~

### Ejemplo
~~~json
{
  "sub_grade": "B4", 
  "int_rate": 15, 
  "out_prncp": 20000
}
~~~

## Acerca de la creación
Este componente backend de la aplicación está creado con el framework minimalista de flask. Para saber más a cerca de Flask

- [Documentación de Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Inicio rapido](https://flask.palletsprojects.com/en/2.1.x/quickstart/)