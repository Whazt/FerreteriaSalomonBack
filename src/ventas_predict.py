import pandas as pd
from sklearn.linear_model import LinearRegression
from db import obtener_conexion

def generar_informe_ventas():
    conexion = obtener_conexion()
    query = "SELECT FehaVenta, Total FROM Ventas"
    df = pd.read_sql(query, conexion)
    df['FechaVenta'] = pd.to_datatime(df['FechaVenta'])
    df['Mes'] = df['FechaVenta'].dt.month
    df['Año'] = df['FechaVenta'].dt.year


#Entrenamiento del modelo de regresión
    x=df[['Año', 'Mes']]
    y= df['Total']
    modelo= LinearRegression()
    modelo.fit(x,y)

    #prediccion 

    prediccion = modelo.predict([[2024, 11]])[0]

    #Resumen del informe
    resumen = df.groupby(['Año','Mes' ])['Total'].sum().reset_index()
    return {
        "resumen" : resumen.to_dict(orient='records'),
        "prediccion" : round(prediccion, 2)
    }
