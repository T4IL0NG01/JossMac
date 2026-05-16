#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random

def crear_carpeta_si_no_existe(ruta):
    """Crea la carpeta si no existe"""
    if not os.path.exists(ruta):
        os.makedirs(ruta)

def generar_mac_aleatorio(prefijo):
    """Genera una MAC completa a partir de un prefijo"""
    # Generar 3 pares hexadecimales aleatorios (para los últimos 3 bytes)
    sufijo = ':'.join([f"{random.randint(0, 255):02X}" for _ in range(3)])
    return f"{prefijo}{sufijo}"

def generar_mac_completa_aleatoria():
    """Genera una MAC completa aleatoria (sin prefijo fijo)"""
    return ':'.join([f"{random.randint(0, 255):02X}" for _ in range(6)])

def generar_combos_mac():
    """Función principal para generar combos MAC"""
    
    # Mostrar JOSS
    print("JOSS")
    print("=" * 40)
    
    # Lista de prefijos MAC
    yeninesil = (
        "00:1A:79:",
        "33:44:CF:",
        "10:27:BE:",
        "A0:BB:3E:",
        "00:1a:79:",
    )
    
    # Menú de opciones
    print("\n📋 TIPOS DE MAC:")
    print("1 - MAC con prefijos de la lista")
    print("2 - MAC completamente aleatoria")
    print("3 - MAC con prefijo personalizado")
    
    # Seleccionar tipo
    while True:
        try:
            tipo = input("\nSelecciona tipo (1/2/3): ").strip()
            if tipo in ["1", "2", "3"]:
                break
            else:
                print("❌ Opción inválida. Elige 1, 2 o 3")
        except KeyboardInterrupt:
            print("\n\n❌ Cancelado")
            return
    
    # Configurar prefijo si es necesario
    prefijo_personalizado = None
    if tipo == "1":
        print(f"\n📌 Prefijos disponibles: {', '.join(yeninesil)}")
    elif tipo == "3":
        prefijo_personalizado = input("Ingresa tu prefijo (ejemplo: AA:BB:CC: ): ").strip().upper()
        if not prefijo_personalizado.endswith(":"):
            prefijo_personalizado += ":"
        print(f"✅ Prefijo configurado: {prefijo_personalizado}")
    
    # Nombre del archivo
    while True:
        nombre_archivo = input("\n📄 Nombre del archivo (sin extensión): ").strip()
        if nombre_archivo:
            # Eliminar caracteres no deseados
            nombre_archivo = "".join(c for c in nombre_archivo if c.isalnum() or c in "._-")
            if nombre_archivo:
                break
        print("❌ Nombre inválido. Usa solo letras, números, puntos, guiones o guión bajo")
    
    # Cantidad a generar
    while True:
        try:
            cantidad = int(input("🔢 Cantidad de MACs a generar: ").strip())
            if cantidad > 0:
                break
            else:
                print("❌ La cantidad debe ser mayor a 0")
        except ValueError:
            print("❌ Ingresa un número válido")
        except KeyboardInterrupt:
            print("\n\n❌ Cancelado")
            return
    
    # Ruta donde guardar el archivo
    ruta_guardado = "/storage/emulated/0/combo/"
    archivo_salida = os.path.join(ruta_guardado, f"{nombre_archivo}.txt")
    
    # Crear la carpeta si no existe
    crear_carpeta_si_no_existe(ruta_guardado)
    
    # Generar MACs
    macs_generadas = []
    print(f"\n🔄 Generando {cantidad} MACs...")
    print("-" * 40)
    
    for i in range(cantidad):
        if tipo == "1":
            prefijo_aleatorio = random.choice(yeninesil)
            mac_completa = generar_mac_aleatorio(prefijo_aleatorio)
        elif tipo == "2":
            mac_completa = generar_mac_completa_aleatoria()
        else:  # tipo == "3"
            mac_completa = generar_mac_aleatorio(prefijo_personalizado)
        
        macs_generadas.append(mac_completa)
        
        # Mostrar progreso cada 100 MACs o si son pocas
        if cantidad <= 20 or (i + 1) % 100 == 0 or i + 1 == cantidad:
            print(f"[{i+1}/{cantidad}] {mac_completa}")
    
    # Guardar en archivo
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            for mac in macs_generadas:
                f.write(mac + '\n')
        
        print("-" * 40)
        print(f"\n✅ ÉXITO!")
        print(f"📁 {cantidad} MACs guardadas en:")
        print(f"📍 {archivo_salida}")
        
        # Mostrar primeras 5 MACs como vista previa
        print("\n📌 Vista previa de las primeras 5 MACs:")
        for i, mac in enumerate(macs_generadas[:5], 1):
            print(f"   {i}. {mac}")
        
        if cantidad > 5:
            print(f"   ... y {cantidad - 5} más")
        
    except Exception as e:
        print(f"\n❌ Error al guardar archivo: {e}")
        return False
    
    return True

if __name__ == "__main__":
    try:
        generar_combos_mac()
    except KeyboardInterrupt:
        print("\n\n❌ Programa cancelado por el usuario")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")