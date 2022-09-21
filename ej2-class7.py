import time

hora=time.strftime('%H')
minutos=time.strftime('%M')
segundos=time.strftime('%S')
if int(hora)>=19:
    print("Es hora de ir a casa")
else:
    print("Faltan {} horas, {}minutos y {} segundos para ir a casa ".format(18- int(hora), 59- int(minutos), 59- int(segundos)))

