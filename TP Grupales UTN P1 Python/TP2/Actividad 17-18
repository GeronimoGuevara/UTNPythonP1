class FuncionesProgramas:
    
    @staticmethod
    def getFechaString(fecha):
    
        fecha = fecha.replace('-','/') 
        dia, mes, anio = fecha.split("/") #Ahora son variables: dia = 15 ; mes = 10 ; anio = 1900
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)
        
        unidades = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        decena_unidad = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
        decenas = ["veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
        veinte = ["veintiuno", "veintidos", "veintitres", "veinticuatro", "veinticinco", "veintiseis", "veintisiete", "veintiocho","veintinueve"]
        centenas = ["ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre","Octubre","Noviembre","Diciembre"]
        
        def convertir_año(parte_del_anio):
                        
            if parte_del_anio == 0:
                return ""
            elif parte_del_anio < 10:
                return unidades[parte_del_anio-1]
            elif parte_del_anio < 20:
                return decena_unidad[parte_del_anio - 10] #le saca la decena
            elif parte_del_anio < 100:
                decena = parte_del_anio // 10
                unidad = parte_del_anio % 10
                if unidad == 0:
                    return decenas[decena - 2]
                else:
                    if decena == 2:
                        return veinte[unidad-1]
                    else:
                        return decenas[decena - 2] + " y " + unidades[unidad-1]
            elif parte_del_anio < 1000:
                centena = parte_del_anio // 100
                resto = parte_del_anio % 100
                if resto == 0:
                    return centenas[centena - 1]
                else:
                    return centenas[centena - 1] + " " + convertir_año(resto)
                
        
        if dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and anio > 0 and anio <= 999999:
            #DIA
            if dia < 10:
             dia = unidades[dia-1].capitalize()
            else:
                if dia < 20:
                    dia = decena_unidad[dia-10].capitalize()
            
            #MES
            mes = meses[mes-1]
            
            #AÑO
            if anio <= 999:
                anio = convertir_año(anio)
            elif anio >= 1000:
                miles = anio // 1000
                resto = anio % 1000
                if miles == 1:
                    anio = "mil " + convertir_año(resto)
                else:
                    if miles > 1 and resto > 0:
                        anio = convertir_año(miles) + " mil " + convertir_año(resto)
                    else:
                        if miles > 1 and resto == 0:
                            anio = convertir_año(miles) +  " mil "
                            
            return f"Fecha escrita literalmente: {dia} de {mes} del año {anio}"  
        else:
             return f"ERROR: Ingrese valores válidos"
      
    #ACTIVIDAD DIECIOCHO(18):
    @staticmethod
    def getFechaDate(dia,mes,anio):
        
        if dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and anio > 0 and anio <= 999999:

            date = [dia, mes, anio]
            
            date = '/'.join(map(str, date))
            
            return f"En formato fecha es: {date}"
        else:
            return f"ERROR: Ingrese valores válidos"
        
        
class Principal:
    
    def main():
        
        fecha = input("Ingrese una fecha a ser escrita literalmente. NOTA: El formato debe ser día/mes/año ")
        fecha_string = FuncionesProgramas.getFechaString(fecha)
        print(fecha_string) 
        
        #ACTIVIDAD DIECIOCHO(18):
        dia = int(input("Ingrese un día del mes "))
        mes = int(input("Ingrese un mes del año "))
        anio = int(input("Ingrese un año "))
        
        fecha_date = FuncionesProgramas.getFechaDate(dia,mes,anio)
        print(fecha_date)
        
#Ejecutar
Principal.main()
