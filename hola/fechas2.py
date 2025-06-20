enero = 31
febrero = 28 
marzo = 31
abril = 30 
mayo = 31 
junio = 30 
julio = 31
agosto = 31 
setptiembre = 30
octubre = 31
noviembre = 30
diciembre = 31

dia_nac = 11
mes_nac = junio
año_nac = 2009

dia_hoy = 5
mes_hoy = febrero
año_actual = 2025

print(2025-2009)
dias_restantes_naci = 365-enero-febrero-dia_nac
print(dias_restantes_naci)
dias_transcurridos_actual = enero+dia_hoy
print(dias_transcurridos_actual)
dias_vividos = 365*(año_actual-año_nac-1)+dias_restantes_naci+dias_transcurridos_actual
print(dias_vividos)
from datetime import datetime
ahora = datetime.now()
print(ahora.year)#año de hoy 
print(ahora.strftime('%A'))#dia de hoy
fecha = datetime(2025,10,4)
print(fecha.strftime('%B'))#mes de una fecha
str_fecha = '11/4/25 11:58:30'
fecha_obj = datetime.strptime(str_fecha, '%d/%m/%y %H:%M:%S')
print(fecha_obj)

