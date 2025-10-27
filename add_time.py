def add_time(start, duration, start_day=None):
    # Separar start
    time_part, periodo = start.split()
    horas, minutos = map(int, time_part.split(":"))
    periodo = periodo.upper()

    # Separar duration
    dur_horas, dur_minutos = map(int, duration.split(":"))

    # Sumar minutos y ajustar horas
    minutos_total = minutos + dur_minutos
    horas_extra = minutos_total // 60
    minutos_final = minutos_total % 60

    horas_total = horas + dur_horas + horas_extra

    # Calcular días y cambios de periodo
    dias = horas_total // 24
    horas_restantes = horas_total % 24

    # Contar los cambios de AM/PM
    cambios_periodo = ((horas // 12) + (horas_total // 12)) % 2
    # Determinar el periodo final
    if cambios_periodo % 2 == 1:
        periodo = "PM" if periodo == "AM" else "AM"
        if periodo == "AM":
            dias += 1

    # Ajustar horas en formato 12h
    horas_final = horas_restantes % 12
    if horas_final == 0:
        horas_final = 12

    # Calcular día de la semana si se da
    if start_day:
        dias_semana = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        indice_inicial = dias_semana.index(start_day.capitalize())
        indice_final = (indice_inicial + dias) % 7
        nuevo_dia = dias_semana[indice_final]

    # Construir resultado
    resultado = f"{horas_final}:{minutos_final:02d} {periodo}"
    if start_day:
        resultado += f", {nuevo_dia}"
    if dias == 1:
        resultado += " (next day)"
    elif dias > 1:
        resultado += f" ({dias} days later)"

    return resultado