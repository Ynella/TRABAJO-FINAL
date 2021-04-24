#!/usr/bin/env python
# coding: utf-8

# # <div style="text-align:center"><span style="color:blue"> TRABAJO FINAL DE LENGUAJES DE PROGRAMACION II</span> </div> 
# 
# ## <div ><span style="color:blue"> Integrantes:</span> </div>
# 1. Llalle Correa Danixa
# 2. Matos Salazar Ruben
# 3. Montoya Toribio Jenny Antonella
# 4. Morales Morales Flavio Oscar
# 
# <span style="color:green;"> Semestre: 2021-2</span>
# ### <div ><span style="color:blue"> Indicaciones </span> </div>
# - El trabajo es grupal (integrantes de grupos ya indicados)
# - Utilizar Jupyter notebook.
# - Trabajar en equipo vía GitHub entre los miembros de los grupos. (Sugerencia: el jefe de grupo puede crear el repositorio del proyecto e invitar a los
# demás integrantes a colaborar en el proyecto).
# 
# ### <div ><span style="color:blue"> Procedimiento Referencial</span> </div>
# 1. Descargar y explorar el archivo genes identificados con vecinos.xlsx compuesta por varias hojas las cuales tienen una columna con etiqueta: GenAbrev.
# 2. Para cada nombre del gen en abreviado (GenAbrev), abrir la página https://www.uniprot.org y en el buscador solicitar la búsqueda de cada una de la forma siguiente: colocar el nombre del gen y la palabra Bos Taurus. Abajo se muestra para UBA52 Bos taurus.
# 3. Se mostrará una lista de genes con el nombre buscado. Extraer información de entry y entry name.
# 4. Seleccionar la primera opción del gen de la primera columna “entry” (clickear), la cual llevará a la siguiente pantalla y de la cual extraer la información de Protein, Gene,Organism y Status.
# 5. Extarer la infomación que corresponde a: GO - Biological process.
# 

# In[3]:


from bs4 import BeautifulSoup
import requests                    #importamos libreria request
import pandas as pd                #importamos la libreria pandas 

GA=input("Introdusca el Gen Abrev: ")
URL=f"https://www.uniprot.org/uniprot/?query={GA.upper()}+bos+taurus&sort=score"
page=requests.get(URL)
soup=BeautifulSoup(page.content,"html.parser")

link_entry=soup.find_all("td",class_="entryID")
indice=[]
for i in link_entry:
    indice.append(i.text)
try:
    FINAL=indice[0]
    url=f"https://www.uniprot.org/uniprot/{FINAL}"
    url="https://www.uniprot.org/uniprot/F1MII5"
    page=requests.get(url)
    soup=BeautifulSoup(page.content,"html.parser")

    #ENTRY Y ENTRY NAME
    entry_name=soup.find_all("h2",class_="page-title")
    for i in entry_name:
        entry1=i.text
    entry1=entry1.split()
    ENTRY=entry1[2]
    ENTRY_NAME="".join(list(entry1[3])[1:len(list(entry1[3]))-1])
    
    print("Entry:",ENTRY)
    print("Entry Name:",ENTRY_NAME)

    #PROTEINA
    protein=soup.find_all("h1",property="name")
    for i in protein:
        PROTEIN=i.text
        
    print("Protein:",PROTEIN)
    
    #GEN
    gen_abrev=soup.find_all("div",class_='entry-overview-content',id="content-gene")
    for i in gen_abrev:
        GEN_ABREV=i.text
    
    print("Gen:",GEN_ABREV)

    #ORGANISMO
    organismo=soup.find_all("div",class_='entry-overview-content',id="content-organism")
    for i in organismo:
        ORGANISMO=i.text
        
    print("Organismo:",ORGANISMO)

    #STATUS
    status=soup.find_all("span",class_='context-help bin-score tooltipped-click')
    for i in status:
        STATUS_PRE=i.text
    STATUS=STATUS_PRE.split("\n")[0].split(":")[1]
    
    print("Status:",STATUS)

    #GO BIOLOGICAL PROCESS
    bio_process=soup.find_all("a",onclick="window.ga('UniProt-Entry-View', 'click', 'Display-GO-Term');")
    BIO_PROCESS=[]
    for i in bio_process:
        BIO_PROCESS.append(i.text)
        
    print("Bio Process:",BIO_PROCESS)

except:
    ENTRY=""
    ENTRY_NAME=""
    PROTEIN=""
    GEN_ABREV=""
    ORGANISMO=""
    STATUS=""
    BIO_PROCESS=""
    print("Entry:",ENTRY)
    print("Entry Name:",ENTRY_NAME)
    print("Protein:",PROTEIN)
    print("Gen:",GEN_ABREV)
    print("Organismo:",ORGANISMO)
    print("Status:",STATUS)
    print("Bio Process:",BIO_PROCESS)

