from pyDatalog import pyDatalog

# Definir términos (predicados y variables)
pyDatalog.create_terms('Organismo, Metodo, SeReproduceAsexualmente, SeReproduceSexualmente')
pyDatalog.create_terms('TieneCiclo, X, Y')

# Definir organismos
Organismo('Protozoo')
Organismo('Bacteria')
Organismo('Alga')

# Definir métodos de reproducción
SeReproduceAsexualmente('Protozoo')
SeReproduceSexualmente('Protozoo')
SeReproduceAsexualmente('Bacteria')
SeReproduceAsexualmente('Alga')
SeReproduceSexualmente('Alga')

# Métodos específicos de reproducción
Metodo('Ameba', 'FisionBinaria')
Metodo('Paramecio', 'Conjugacion')
Metodo('EscherichiaColi', 'FisionBinaria')
Metodo('Ulva', 'AlternanciaDeGeneraciones')
Metodo('Spirogyra', 'Fragmentacion')
Metodo('Plasmodium', 'Esquizogonia')

# Definir ciclos de vida en algas
TieneCiclo('Ulva', 'AlternanciaDeGeneraciones')

# Función para consultar reproducción
def consulta_reproduccion():
    print("\n🔎 Organismos registrados:")
    print(Organismo(X))

    print("\n🔬 Organismos con reproducción asexual:")
    print(SeReproduceAsexualmente(X))

    print("\n🧬 Organismos con reproducción sexual:")
    print(SeReproduceSexualmente(X))

    print("\n🦠 Métodos de reproducción por organismo:")
    print(Metodo(X, Y))

    print("\n🌱 Ciclos de vida de algunas algas:")
    print(TieneCiclo(X, Y))

# Ejecutar consulta
if __name__ == "__main__":
    consulta_reproduccion()
