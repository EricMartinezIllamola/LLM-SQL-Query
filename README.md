# LLM-SQL

- Link a la App: https://ericmartinezillamola-llm-sql.streamlit.app/

## Introducción

Este proyecto consiste en la creación de una aplicación que, a partir de una pregunta realizada en lenguaje natural por el usuario, sea capaz de realizar consultas SQL en una base de datos. Ante todo, el principal objetivo es aprender nuevas tecnologías, practicar y consolidar conocimientos. 

## Planteamiento

La mayoría de empresas, y organizaciones en general, almacenan sus datos en bases de datos. La función principal de esta aplicación es responder a preguntas realizadas en lenguaje natural, basándose en los datos almacenados en una base de datos (SQLite en este caso).

Existen varias aproximaciones posibles. Inicialmente, lo que parecía más conveniente era que la herramienta de LLM (por ejemplo, SQLDatabaseChain o sql_agent) realizase todos los pasos por sí misma (pregunta --> SQL Query --> resultado de la Query --> respuesta final). Pero esta aproximación tiene varios inconvenientes, por ejemplo: 

- No permite obtener los resultados de los pasos intermedios, o por lo menos no fácilmente. 

- Los resultados de algunas consultas SQL pueden ser muy extensos (obtener una tabla con varias filas y columnas, y no simplemente un número), por lo tanto, que la respuesta final del bot fuese en lenguaje natural, originaba una respuesta final poco legible.

## Funcionamiento

Finalmente, se ha optado por una aproximación más customizable, sql_query_chain, una herramienta LLM que simplemente realiza el primer paso (pregunta --> SQL Query). El resto de pasos se realizan de forma "manual". Esto permite obtener la SQL Query, ejecutarla y mostrar el resultado final en un formato más idóneo (en forma de dataframe).

Mediante el prompt, se proporcionan instrucciones detalladas al bot para que realice su función correctamente. Para mejorar su rendimiento, en el prompt, también se la proporciona la siguiente información:

- La sentencia CREATE TABLE utilizada para crear cada tabla, que incluye el nombre de las columnas, el tipo de datos de las columnas...

- Tres ejemplos de filas de cada tabla (mediante una sentencia SELECT).

- Varias preguntas a modo de ejemplo, así como su correspondiente SQL Query.

En resumen, en la sección '🤖Text to SQL Query', el usuario realiza una pregunta en lenguaje natural y el bot retorna una sentencia SQL que permite obtener los datos requeridos por el usuario al ejecutarla, resultado que se muestra en pantalla en forma de tabla para mejor conveniencia del usuario. La respuesta final (la tabla) se puede descargar en formato CSV si se desea. También se puede comprobar la SQL Query utilizada para obtener ese resultado.

## Funciones Adicionales

Además de la sección principal ('🤖Text to SQL Query'), existen dos secciones adicionales:

- '💻Database Info': Esta sección sirve para que el usuario pueda obtener información básica sobre la base de datos (nombre y número de filas de cada tabla, nombre de las columnas, tipo de dato de las columnas, conexiones entre tablas...).

- '👩‍🎓Practice Yourself': Esta sección permita al usuario realizar consultas SQL directamente (escribiendo la SQL Query en sí). El usuario la puede utilizar de la forma que crea más conveniente, pero se han añadido varias opciones que le permiten practicar y poner a prueba las habilidades SQL. La idea es que se haga una pregunta al bot en la sección '🤖Text to SQL Query' y posteriormente (sin mirar la SQL Query resultante) se intente replicar el dataframe ofrecido por el bot.

## Base de Datos

Se ha utilizado una base de datos SQLite por razones de comodidad: la base de datos SQLite es un fichero subido en el repositorio y de esta forma no hace falta utilizar una plataforma de hosting para bases de datos.

La base de datos contiene datos ficticios sobre InnovaTech, una compañía distribuidora de ordenadores mayorista (también ficticia). En el repositorio se ha añadido el script de creación de la base de datos, aunque no sea necesario para el funcionamiento de la App en sí. Aunque se trata de datos ficticios, se ha intentado que sean lo máximo realistas y consistentes posibles.

Las SQL Queries a la base de datos se realizan en modo solo lectura (ReadOnly), para evitar modificaciones indeseadas.

## Tecnologías

Principales tecnologías utilizadas: LangChain, GooglePaLM, sqlite3 y Streamlit.

Para más información sobre cómo utilizar LangChain, LLM y SQL conjuntamente: https://python.langchain.com/docs/use_cases/qa_structured/sql