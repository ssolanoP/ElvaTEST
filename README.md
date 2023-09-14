# ElvaTEST
Prueba Técnica Elva Costa Rica
Para la realización de la prueba fue necesario crear una AppiKey que solicita google para poder usar su API de google MAPS.

Dentro los métodos que ofrece google maps se encontraron 2 operaciones fundamentales para el desarrollo de la prueba técnica, la primera de ellas "geocode" y la segunda "reverse_geocode" 
dichos métodos fueron utlizados para sacar la longitud y latitud de la dirección inicial y para codificar desde la longitud y latitud las posibles localizaciones que se encontraban a las mismas.

Para el primer item se genera el código para que se pueda validar el vecindario o barrio que corresponde a dichas coordenadas.

Dentro de la api de google maps para el método "geocode" se genera la siguiente estructura de datos. 
Aquí muestra las descripciones de la dirección solicitada dentro de la prueba técnica.

![image](https://github.com/ssolanoP/ElvaTEST/assets/140436208/0cf3ff2c-caff-49d4-b0f0-0b5589c99bce)


Ahora para el método "reverse_geocode" se genera la siguiente estructura de datos, la cual describe la construcción de la ubicación con a las coordenadas dadas desde el primer método.

![image](https://github.com/ssolanoP/ElvaTEST/assets/140436208/7b74cb0a-e88a-4af7-9f30-ac9d0689c7e9)


Aquí se muestra la API creada por parte mía para la interpretación de esas coordenadas.

![image](https://github.com/ssolanoP/ElvaTEST/assets/140436208/f6447bae-222e-4eab-a994-efd253281231)


En esta siguiente imagen se muestra la respuesta de la función recursiva para validar el vecindario que limita con el vecindario encontrado en el primer item.

![image](https://github.com/ssolanoP/ElvaTEST/assets/140436208/cccec416-25d0-4117-9fb1-b2efa2a85dd8)


