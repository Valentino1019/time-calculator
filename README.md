# Time Calculator (Python)

Calculadora de tiempo que permite sumar duraciones a horas iniciales en formato 12h (AM/PM), mostrando el resultado con cambios de días y, opcionalmente, el día de la semana.

## Descripción

Este proyecto implementa la función `add_time()` que recibe:
- **start**: hora inicial en formato 12h (ej: `"3:00 PM"`)  
- **duration**: duración a sumar en horas y minutos (ej: `"2:30"`)  
- **starting_day** *(opcional)*: día de la semana en que comienza (ej: `"Monday"`)

La función devuelve el tiempo final con:
- AM/PM actualizado
- Día de la semana si se proporciona
- Número de días transcurridos si es más de un día

Este proyecto permite practicar:
- Manipulación de cadenas (`split`, `join`)
- Conversión entre texto y números
- Aritmética de tiempo
- Condicionales y lógica
- Uso de funciones y retorno de valores
- Formateo de salida con `f-strings`

---

## Ejemplos de uso

```python
from add_time import add_time

print(add_time('3:00 PM', '3:10'))
# Salida: 6:10 PM

print(add_time('11:43 PM', '24:20', 'Tuesday'))
# Salida: 12:03 AM, Thursday (2 days later)

print(add_time('10:10 PM', '3:30'))
# Salida: 1:40 AM (next day)

print(add_time('6:30 PM', '205:12'))
# Salida: 7:42 AM (9 days later)
```

---

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/time-calculator.git
   ```
2. El archivo principal es `add_time.py`. No requiere librerías externas.

---

## Pruebas

Para probar la función, puedes usar el archivo de ejemplos o ejecutar tus propios casos en un script de Python.

---

## Créditos

Proyecto basado en el curso de Python de [freeCodeCamp](https://www.freecodecamp.org/).

---

## Licencia

Este proyecto se publica bajo la licencia MIT.  