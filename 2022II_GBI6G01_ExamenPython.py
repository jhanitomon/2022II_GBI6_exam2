#!/usr/bin/env python
# coding: utf-8

# <img src="https://th.bing.com/th/id/OIP.5u5ytRTR7hcp6FEWEBHLqwAAAA?pid=ImgDet&rs=1" width=300 height=240 />
# <font color='red'></font>
# 
# # EXAMEN PARCIAL PYTHON
#     
# 
# ## GBI6-2022II: BIOINFORMÁTICA
# 
# **Torres, Jhanina** <font color='red'></font>
# 
# **01-02-2022**
# 
# | CARACTERISTICAS DEL EQUIPO | | |
# | --- | --- | --- |
# |Nombre del dispositivo                LAB-D-E32 |  |  |
# |Procesador                            Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz   3.60 GHz|  |  |  
# |Identificador de dispositivo          863752D5-95CC-4316-AF89-6EDA541E1338|  |  |
# |Id. del producto                      00330-80000-00000-AA932|  |  |    
# |Tipo de sistema Sistema operativo de 64 bits, procesador basado en x64|  |  |
# |Lápiz y entrada táctil La entrada táctil o manuscrita no está disponible para esta pantalla|  |  |

# ### REQUERIMIENTOS PARA EL EXAMEN
# 
# Utilice de preferencia ```Jupyter``` de Anaconda, dado que tienen que hacer un control de cambios en cada pregunta. 
# 
# Para este examen se requiere dos documentos: 
# 
# 1. Archivo ```coati.py``` donde tendrá dos funciones:
# 
# 2. Archivo ```2022II_GBI6_ExamenPython``` donde se llamará las funciones y se obtendrá resultados.

# ## Ejercicio 0 [0.5 puntos]
# Realice cambios al cuaderno de jupyter: 
# - Agregue el logo de la Universidad
# - Coloque sus datos personales 
# - Escriba una <font color='red'>**tabla**</font> con las características de su computador 
# 
# 

# ## Ejercicio 1 [1.5 puntos]
# Inserte la captura de pantalla del curso [PANDAS](https://www.kaggle.com/learn/pandas) de Kaggle (Certificado y evidencia de avance de la página de Kaggle)

# <img src="http://localhost:8888/files/Users/aula/Downloads/WhatsApp%20Image%202023-01-31%20at%2010.34.35%20AM.jpeg" width=300 height=240 />

# ## Ejercicio 2 [1.5 puntos]
# Inserte la captura de pantalla del curso [VISUALIZACIÓN](https://www.kaggle.com/learn/data-visualization) de Kaggle (Certificado y evidencia de avance de la página de Kaggle)

# <img src="http://localhost:8888/files/Users/aula/Downloads/WhatsApp%20Image%202023-02-01%20at%207.11.33%20PM.jpeg" width=300 height=240 />

# ## Ejercicio 3 [3 puntos]
# 
# En su carpeta de examen tiene el documento ```id_coati.txt``` donde se encuentran los identificadores de accesión que debe usar para descargar información. 
# Cree el módulo ```coati.py``` con las siguientes tres **funciones** y sus respectivos **docstring** :
#     
# i. ```fasta_downloader```: para cargar ```id_coati.txt``` en ```id_coati```y descargar en **formato genbank** la información correspondiente a los identificadores de accesión usando el **ENTREZ** de Biopythony se guardar en ```coati``` y en ```coati.gb```. 
# 
# ii. ```alignment```: para que el algoritmo extraiga **solamente las secuencias** de la variable ```coati``` y realice un alineamiento usando clustalW. El resultado debe ser ```coati.aln``` y ```coati.dnd``` que deben guardarse en su carpeta de trabajo.  
# 
# iii ```tree```: para que realice el cálculo de las distancias utilizando ```coati.aln``` y finalmente que imprima en la pantalla el árbol filogenético y guarde en su carpeta de trabajo el arbol como ```coati_phylotree.pdf```
# 
# iv. Cargue el módulo ```coati``` e **imprima docstring de cada función**.
# 

# In[1]:


# Escriba aquí su código para el ejercicio 3










# 
# ## Ejercicio 4 [1.5 puntos]
# 
# Escriba una o dos líneas de código para usar las funciones ```fasta_downloader```, ```alignment``` y ```tree```: 
# 
# i. Descargue la data en ```coati``` y guarde como ```coati.gdb```.  
# 
# ii. Alinee las secuencias de ```coati``` y obtenga ```coati.aln``` y ```coati.dnd```.
# 
# iii. Construya e **interprete** el arbol filogenético y guarde en ```coati_phylotree.pdf```.

# In[2]:


# Escriba aquí su código para el ejercicio 4


# ## Ejercicio 5 [1.5 puntos]
# 
# Con las secuencias de ADN de ```coati```, realice lo siguiente: 
# 
# i. la traducción y cálculo del peso molecular (**molecular_weight**) y el índice de estabilidad (**instability_index**) de los péptidos resultantes. 
# 
# ii. una gráfica tipo [joinplot](https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot) utilizando los parámetros de peso molecular e índice de estabilidad. Edite color, tamaño y tipo de puntos, asimismo etiquete adecuadamente el título y los ejes.
# 
# iii. guarde la figura como ```coati.png``` con una resolución de 300dpi.
# 
# iv. interprete la figura resultante

# In[4]:


# Escriba aquí su código para el ejercicio 5
















# ## Ejercicio 6 [0.5 puntos]
# 
# 
# 1. Cree un archivo ```Readme.md``` que debe tener lo siguiente:
# - Datos personales
# - Características del computador
# - Versión de Python/Anaconda y de cada uno de los módulos/paquetes y utilizados
# - Explicación de la data utilizada
# 
# 2. Asegurarse que su repositorio tiene las carpetas ```data``` e ```img``` con los archivos que ha ido guardando en las preguntas anteriores.  
# 3. Realice al menos 1 control de la versión (commits) por cada ejercicio (del 1 al 5), con un mensaje que inicie como: 
# 
# ```sh 
# Carlitos Alimaña ha realizado el ejercicio 1  
# ```
# ```sh 
# Carlitos Alimaña ha realizado el ejercicio 2
# ```
# ```sh 
# ...
# ```
# 

# In[ ]:




