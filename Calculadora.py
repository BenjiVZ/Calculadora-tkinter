import math
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

# Función para convertir longitud
def convertir_longitud(valor, unidad_origen, unidad_destino):
    unidades_longitud = {
        "Metros": 1,
        "Centímetros": 0.01,
        "Milímetros": 0.001,
        "Pies": 0.3048,
        "Yardas": 0.9144,
        "Millas": 1609.344
    }
    factor_conversion = unidades_longitud[unidad_destino] / unidades_longitud[unidad_origen]
    return valor * factor_conversion

# Función para convertir capacidad
def convertir_capacidad(valor, unidad_origen, unidad_destino):
    unidades_capacidad = {
        "Litros": 1,
        "Mililitros": 0.001,
        "Galones": 3.785411784,
        "Cuartos": 0.946352946,
        "Pintas": 0.473176473,
        "Onzas": 29.57352957
    }
    factor_conversion = unidades_capacidad[unidad_destino] / unidades_capacidad[unidad_origen]
    return valor * factor_conversion

# Función para convertir masa
def convertir_masa(valor, unidad_origen, unidad_destino):
    unidades_masa = {
        "Kilogramos": 1,
        "Gramos": 0.001,
        "Miligramos": 0.000001,
        "Libras": 0.45359237,
        "Piedras": 6.35029318
    }
    factor_conversion = unidades_masa[unidad_destino] / unidades_masa[unidad_origen]
    return valor * factor_conversion

#funcion para la calculadora 
def mostrar_calculadora():
    resultado_label.config(text="")
    numero_1 = simpledialog.askfloat("Calculadora Básica", "Ingrese el primer número:")
    if numero_1 is not None:
        numero_2 = simpledialog.askfloat("Calculadora Básica", "Ingrese el segundo número:")
        if numero_2 is not None:
            operacion = simpledialog.askstring("Calculadora Básica", "Ingrese la operación (+, -, *, /):")
            if operacion is not None:
                if operacion == "+":
                    resultado = numero_1 + numero_2
                elif operacion == "-":
                    resultado = numero_1 - numero_2
                elif operacion == "*":
                    resultado = numero_1 * numero_2
                elif operacion == "/":
                    if numero_2 != 0:
                        resultado = numero_1 / numero_2
                    else:
                        messagebox.showerror("Error", "División por cero no permitida")
                        return
                else:
                    messagebox.showerror("Error", "Operación incorrecta")
                    return
                resultado_label.config(text=f"El resultado es: {resultado}")

#funcion para convertir temperatura
def mostrar_conversor_temperatura():
    resultado_label.config(text="")
    unidad_medida = mostrar_ventana_dialogo(["Celsius (C)", "Fahrenheit (F)"], "Conversor de Temperatura", "Escoja la unidad de medida:")
    if unidad_medida is not None:
        temperatura = simpledialog.askfloat("Conversor de Temperatura", "Ingrese la temperatura:")
        if temperatura is not None:
            if "C" in unidad_medida:
                temperatura_convertida = (temperatura * 9/5) + 32
                unidad_medida_convertida = "Fahrenheit"
            elif "F" in unidad_medida:
                temperatura_convertida = (temperatura - 32) * 5/9
                unidad_medida_convertida = "Celsius"
            resultado_label.config(text=f"La temperatura convertida es: {temperatura_convertida} {unidad_medida_convertida}")

#funcion para calcular el area
def mostrar_calculadora_area():
    resultado_label.config(text="")
    figura_geometrica = mostrar_ventana_dialogo(["Círculo", "Triángulo", "Rectángulo"], "Calculadora de Área", "Escoja la figura geométrica:")
    if figura_geometrica is not None:
        if "Círculo" in figura_geometrica:
            radio = simpledialog.askfloat("Calculadora de Área", "Ingrese el radio del círculo:")
            if radio is not None:
                area = math.pi * radio ** 2
        elif "Triángulo" in figura_geometrica:
            base = simpledialog.askfloat("Calculadora de Área", "Ingrese la base del triángulo:")
            altura = simpledialog.askfloat("Calculadora de Área", "Ingrese la altura del triángulo:")
            if base is not None and altura is not None:
                area = (base * altura) / 2
        elif "Rectángulo" in figura_geometrica:
            base = simpledialog.askfloat("Calculadora de Área", "Ingrese la base del rectángulo:")
            altura = simpledialog.askfloat("Calculadora de Área", "Ingrese la altura del rectángulo:")
            if base is not None and altura is not None:
                area = base * altura
        resultado_label.config(text=f"El área es: {area}")

#funcion para mostrar numeros pares o impares
def mostrar_numeros_pares_impares():
    resultado_label.config(text="")
    numero = simpledialog.askinteger("Números Pares e Impares", "Ingrese un número entero:")
    if numero is not None:
        if numero % 2 == 0:
            resultado_label.config(text="El número es par")
        else:
            resultado_label.config(text="El número es impar")

#funcion para convertir unidades
def mostrar_conversor_unidades():
    resultado_label.config(text="")
    tipo_conversion = mostrar_ventana_dialogo(["Longitud", "Capacidad", "Masa"], "Convertir Longitud, Capacidad o Masa", "Escoja el tipo de conversión:")
    if tipo_conversion is not None:
        valor = simpledialog.askfloat("Convertir Unidades", "Ingrese el valor:")
        if valor is not None:
            if tipo_conversion == "Longitud":
                unidades = ["Metros", "Centímetros", "Milímetros", "Pies", "Yardas", "Millas"]
            elif tipo_conversion == "Capacidad":
                unidades = ["Litros", "Mililitros", "Galones", "Cuartos", "Pintas", "Onzas"]
            elif tipo_conversion == "Masa":
                unidades = ["Kilogramos", "Gramos", "Miligramos", "Libras", "Piedras"]
            
            unidad_origen = mostrar_ventana_dialogo(unidades, "Convertir Unidades", "Escoja la unidad de origen:")
            unidad_destino = mostrar_ventana_dialogo(unidades, "Convertir Unidades", "Escoja la unidad de destino:")

            if unidad_origen is not None and unidad_destino is not None:
                if tipo_conversion == "Longitud":
                    valor_convertido = convertir_longitud(valor, unidad_origen, unidad_destino)
                elif tipo_conversion == "Capacidad":
                    valor_convertido = convertir_capacidad(valor, unidad_origen, unidad_destino)
                elif tipo_conversion == "Masa":
                    valor_convertido = convertir_masa(valor, unidad_origen, unidad_destino)
                resultado_label.config(text=f"El valor convertido es: {valor_convertido} {unidad_destino}")


def mostrar_ventana_dialogo(opciones, titulo, mensaje):
    ventana_dialogo = tk.Tk()
    ventana_dialogo.title(titulo)
    seleccion = None

    def seleccionar_opcion(opcion):
        nonlocal seleccion
        seleccion = opcion
        ventana_dialogo.quit()

    for opcion in opciones:
        boton = tk.Button(ventana_dialogo, text=opcion, command=lambda o=opcion: seleccionar_opcion(o))
        boton.pack()

    etiqueta = tk.Label(ventana_dialogo, text=mensaje)
    etiqueta.pack()

    ventana_dialogo.mainloop()
    ventana_dialogo.destroy()
    return seleccion

root = tk.Tk()
root.title("Ejercicios de Python")
root.configure(bg='#36393f')

# Creación de estilos con ttk.Style
style = ttk.Style()
style.configure("TButton", padding=(10, 5), relief="flat", background="#7289da", foreground="black")
style.configure("TLabel", background="#36393f", foreground="black")

calculadora_button = ttk.Button(root, text="Calculadora Básica", command=mostrar_calculadora)
conversor_temperatura_button = ttk.Button(root, text="Conversor de Temperatura", command=mostrar_conversor_temperatura)
calculadora_area_button = ttk.Button(root, text="Calculadora de Área", command=mostrar_calculadora_area)
numeros_pares_impares_button = ttk.Button(root, text="Números Pares e Impares", command=mostrar_numeros_pares_impares)
conversor_unidades_button = ttk.Button(root, text="Convertir Longitud, Capacidad o Masa", command=mostrar_conversor_unidades)

resultado_label = ttk.Label(root, text="", font=("Helvetica", 14))  # Utiliza ttk.Label
resultado_label.configure(background="#C4FCF0", foreground="black")  # Establece fondo gris oscuro y texto negro

# Aplica los estilos a los botones
calculadora_button["style"] = "TButton"
conversor_temperatura_button["style"] = "TButton"
calculadora_area_button["style"] = "TButton"
numeros_pares_impares_button["style"] = "TButton"
conversor_unidades_button["style"] = "TButton"

# Alinea los botones a la izquierda
calculadora_button.pack(anchor='w')
conversor_temperatura_button.pack(anchor='w')
calculadora_area_button.pack(anchor='w')
numeros_pares_impares_button.pack(anchor='w')
conversor_unidades_button.pack(anchor='w')
resultado_label.pack()

root.mainloop()
