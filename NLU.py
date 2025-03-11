from pyDatalog import pyDatalog

# Definir los predicados
pyDatalog.create_terms('Organismo, Metodo, Tipo, X')

# Hechos: Definir organismos y sus métodos de reproducción
+ Organismo('Ameba')
+ Tipo('Ameba', 'Protozoo')
+ Metodo('Ameba', 'Fisión Binaria')

+ Organismo('Paramecio')
+ Tipo('Paramecio', 'Protozoo')
+ Metodo('Paramecio', 'Conjugación')

+ Organismo('Plasmodium')
+ Tipo('Plasmodium', 'Protozoo')
+ Metodo('Plasmodium', 'Esquizogonia')

+ Organismo('E_coli')
+ Tipo('E_coli', 'Bacteria')
+ Metodo('E_coli', 'Fisión Binaria')

+ Organismo('Ulva')
+ Tipo('Ulva', 'Alga')
+ Metodo('Ulva', 'Alternancia de Generaciones')

+ Organismo('Spirogyra')
+ Tipo('Spirogyra', 'Alga')
+ Metodo('Spirogyra', 'Fragmentación')

# Consulta de todos los organismos registrados
print("🔎 Organismos registrados:")
print(Organismo(X))

# Consulta de métodos de reproducción de un organismo específico
print("\n🧬 Métodos de reproducción de Ameba:")
print(Metodo('Ameba', X))
