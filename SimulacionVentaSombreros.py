"""Simula un negocio de venta de sombreros operado por Jimena. Calcula las ganancias totales por la
venta de sombreros, basado en la cantidad inicial de sombreros, el precio de venta y la estrategia
de ventas. El script asume que Jimena sigue una estrategia específica de ventas: vender un tercio
de la cantidad inicial primero y luego la mitad de los sombreros restantes. Muestra el estado
inicial y final del negocio, incluyendo la cantidad de sombreros restantes y el total de dinero
en caja después de cada ronda de ventas."""

def main():
    print("Simulacion venta de Sombreros")
    sombreros=int(input("Ingrese una cantidad inicial de sombreros entre 10 y 20: "))
    dinero=1000
    precio=int(input("Ingrese un precio de venta de cada unidad entre 200 y 800: $"))
    cant_venta=sombreros//3

    print("\nJimena tiene",sombreros,"sombreros,los vende a $",precio," cada uno y $",dinero,"en caja.")
    dinero=dinero+(precio*cant_venta)
    print("Vende la tercera parte: ",cant_venta,'sombreros a',precio,'y tiene $',dinero,'en caja.')
    sombreros= sombreros - cant_venta
    cant_venta=sombreros//2
    print('\nVende la mitad de lo restante: ',cant_venta,'sombreros a $',precio,'.')
    dinero=dinero+(cant_venta*precio)
    print('Jimena ahora tiene',sombreros,'sombreros y $',dinero,'en caja.')
main()