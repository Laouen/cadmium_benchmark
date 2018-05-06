from math import ceil

# Las funcinoes links coupleds atomics calcula la cantidad de links coupleds atomics correspondientes a un modelo test
# generado por test/utilities/generate_sbml.py para un tamaño de n reacciones
def links(n):
	groups = ceil((float(n) / 150.0))
	return 6 + 5*2 + 16 + 3 * (groups * 3 + 1) + 2 * (groups * 5 + 1) + (groups * 4 + 1) + 6 * n

def coupleds(n):
    groups = ceil(float(n) / 150)
    return 1 + 3 + 2 * (1 + groups) + 4 + 4 * groups

def atomics(n):
    groups = ceil(float(n) / 150)
    return 3 + 6 + 6 * groups + 6 * n

# remoueve todas las lineas en blanco que tienen el symbolo \r como separador
def remove_empty_lines(path):                  
	f = open(path, 'r')
	a = f.readlines()[0].split('\r')
	a = [l for l in a if l != '']
	f2 = open(path + '.cropted', 'w')
	f2.write('\n'.join(a))
	f2.close()
	f.close()