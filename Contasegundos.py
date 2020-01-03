segundos_str=input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs=int(segundos_str)

dias=total_segs//86400
seg_restantes=total_segs%86400
horas=seg_restantes//3600
segs_restantesdois=seg_restantes%3600
minutos=segs_restantesdois//60
segs_restantes_final=segs_restantesdois%60

print(dias, "dias",horas, "horas", minutos, "minutos e", segs_restantes_final, "segundos")