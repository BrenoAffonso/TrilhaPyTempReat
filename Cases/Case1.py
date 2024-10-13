hora=int(input('Que horas você quer dormir(Se quiser dormir 23:15, responda só 23)\n'))
minuto=int(input('Que minutos você quer dormir(Se quiser dormir 23:15, responda só 15)\n'))

ciclo=90
horaLeap=ciclo//60
minutoLeap=ciclo%60

n=1
while n!=7:
    hora+=horaLeap
    hora=hora%24
    minuto+=minutoLeap
    
    if minuto%60!=minuto:
        hora+=1
        hora=hora%24
        minuto=minuto%60
    
    print(f"Horário {n} para acordar : {hora:02}:{minuto:02}")
    n+=1