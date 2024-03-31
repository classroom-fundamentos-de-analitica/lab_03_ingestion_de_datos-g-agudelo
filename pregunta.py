"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    dic={"cluster":[],"cantidad_de_palabras_clave":[],"porcentaje_de_palabras_clave":[],"principales_palabras_clave":[]}
    with open('clusters_report.txt', mode="r") as cluster:
        archivo = cluster.readlines()
    linea2=""
    for linea in archivo[4:]:
        regex = r"\b\d+(?:,\d+)?(?:\.\d+)?\s"
        result = re.findall(regex,linea)
        if len(result) != 0:
            dic["cluster"].append(int(result[0].strip()))
            dic["cantidad_de_palabras_clave"].append(int(result[1].strip()))
            dic["porcentaje_de_palabras_clave"].append(float(result[2].strip().replace(",",".")))
        regex = r"%\s*(.*?)\n"
        result = re.findall(regex,linea)
        if len(result) != 0:
            linea1 = result[0].replace("  ","")
        if len(result) == 0:
            regex = r"\s*(.*?)\n"
            result = re.findall(regex,linea)
            if result == [""]:
                dic["principales_palabras_clave"].append((linea1+linea2).replace(", ",",").replace(",",", "))
                linea2=""
            else:
                linea2=(linea2+result[0]).replace("  ","").replace(".","")
    df=pd.DataFrame(dic)
    df["principales_palabras_clave"]=df["principales_palabras_clave"]
    return df
print(ingest_data())