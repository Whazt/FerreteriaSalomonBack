import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ventas_predict import generar_informe_ventas

def conectar_google_sheets():
    scope = ["", ""]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credenciales.json", scope)
    cliente = gspread.authorize(creds)
    return cliente

def exportar_a_sheets():
    informe = generar_informe_ventas()
    cliente = conectar_google_sheets()
    hoja = cliente.create("Informe de Ventas")
    worksheet = hoja.get_worksheet(0)

    #Subir Resumen y Prediccion al Sheet
    worksheet.update([["Año", "Mes", "Total"]] + [list(row.values()) for row in informe['resumen']])
    worksheet.append_row(["2024", "11", informe["prediccion"]])

    print("Informe exportado exitosamente a google Sheets.")