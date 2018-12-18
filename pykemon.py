#Creación de la clase Tipo
class Tipo:
    nombre = ''
    resistencias = []
    debilidades = []
    inmunidades = []

#Creación de las instancias de cada tipo
normal = Tipo()
acero = Tipo()
agua = Tipo()
bicho = Tipo()
dragon = Tipo()
electrico = Tipo()
fantasma = Tipo()
fuego = Tipo()
hada = Tipo()
hielo = Tipo()
lucha = Tipo()
planta = Tipo()
psiquico = Tipo()
roca = Tipo()
siniestro = Tipo()
tierra = Tipo()
veneno = Tipo()
volador = Tipo()

#Guardar nombre de cada tipo
normal.nombre = 'Normal'
acero.nombre = 'Acero'
agua.nombre = 'Agua'
bicho.nombre = 'Bicho'
dragon.nombre = 'Dragón'
electrico.nombre = 'Eléctrico'
fantasma.nombre = 'Fantasma'
fuego.nombre = 'Fuego'
hada.nombre = 'Hada'
hielo.nombre = 'Hielo'
lucha.nombre = 'Lucha'
planta.nombre = 'Planta'
psiquico.nombre = 'Psíquico'
roca.nombre = 'Roca'
siniestro.nombre = 'Siniestro'
tierra.nombre = 'Tierra'
veneno.nombre = 'Veneno'
volador.nombre = 'Volador'

#Definición de los tipos existentes
tipos = [normal, acero, agua, bicho, dragon, electrico, fantasma, fuego, hada, hielo, lucha, planta, psiquico, roca, siniestro, tierra, veneno, volador]

#Guardar resistencias de cada tipo
agua.resistencias = [acero, agua, fuego, hielo]
bicho.resistencias = [lucha, planta, tierra]
dragon.resistencias = [agua, electrico, fuego, planta]
electrico.resistencias = [acero, electrico, volador]
fantasma.resistencias = [bicho, veneno]
fuego.resistencias = [acero, bicho, fuego, hada, hielo, planta]
hada.resistencias = [bicho, lucha, siniestro]
hielo.resistencias = [hielo]
lucha.resistencias = [bicho, roca, siniestro]
normal.resistencias = []
planta.resistencias = [agua, electrico, planta, tierra]
psiquico.resistencias = [lucha, psiquico]
roca.resistencias = [fuego, normal, veneno, volador]
siniestro.resistencias = [fantasma, siniestro]
tierra.resistencias = [roca, veneno]
veneno.resistencias = [bicho, hada, lucha, planta, veneno]
volador.resistencias = [bicho, lucha, planta]
acero.resistencias = [acero, bicho, dragon, hada, hielo, normal,                       planta, psiquico, roca, volador]

#Guardar debilidades de cada tipo
agua.debilidades = [electrico, planta]
bicho.debilidades = [fuego, roca, volador]
dragon.debilidades = [dragon, hada, hielo]
electrico.debilidades = [tierra]
fantasma.debilidades = [fantasma, siniestro]
fuego.debilidades = [agua, roca, tierra]
hada.debilidades = [acero, veneno]
hielo.debilidades = [acero, fuego, lucha, roca]
lucha.debilidades = [hada, psiquico, volador]
normal.debilidades = [lucha]
planta.debilidades = [bicho, fuego, hielo, veneno, volador]
psiquico.debilidades = [bicho, fantasma, siniestro]
roca.debilidades = [acero, agua, lucha, planta, tierra]
siniestro.debilidades = [bicho, hada, lucha]
tierra.debilidades = [agua, hielo, planta]
veneno.debilidades = [psiquico, tierra]
volador.debilidades = [electrico, hielo, roca]
acero.debilidades = [fuego, tierra, lucha]

#Inmunidades de cada tipo
acero.inmunidades = [veneno]
fantasma.inmunidades = [lucha, normal]
hada.inmunidades = [dragon]
normal.inmunidades = [fantasma]
siniestro.inmunidades = [psiquico]
tierra.inmunidades = [electrico]
volador.inmunidades = [tierra]


def common(list1, list2):
    return [element for element in list1 if element in list2]


def relacion(tipo_a, tipo_b):
    deb = tipo_a.debilidades + tipo_b.debilidades
    res = tipo_a.resistencias + tipo_b.resistencias + tipo_a.inmunidades + tipo_b.inmunidades + tipo_a.inmunidades + tipo_b.inmunidades
    
    aux_1 = []
    for i in res:
        if i in deb:
            aux_1.append(i)

    aux_2 = []
    for i in deb:
        if i in res:
            aux_2.append(i)

    for i in aux_1:
        if i in deb:
            deb.remove(i)

    for i in aux_2:
        if i in res:
            res.remove(i)

    doble_deb = []
    for i in deb:
        if deb.count(i) >= 2:
            doble_deb.append(i)
    doble_deb = set(doble_deb)
    deb = set(deb)

    doble_res = []
    for i in res:
        if res.count(i) >= 2:
            doble_res.append(i)
    doble_res = set(doble_res)
    res = set(res)

    for i in doble_res:
        res.remove(i)
    for i in doble_deb:
        deb.remove(i)

    if tipo_a == tipo_b:
        res = tipo_a.resistencias
        doble_res = tipo_a.inmunidades
        deb = tipo_a.debilidades
        doble_deb = []
    
    return list(deb), list(doble_deb), list(res), list(doble_res)


def info_equipo(tipo_a_1, tipo_b_1, tipo_a_2, tipo_b_2, tipo_a_3, tipo_b_3):
    """Entrega información sobre el equipo por pantalla.
    
    Parameters
    ----------
    tipo_a_1 : tipo
        Primer tipo del primer Pokémon.
    tipo_b_1 : tipo
        Segundo tipo del primer Pokémon.
    tipo_a_2 : tipo
        Primer tipo del segundo Pokémon.
    tipo_b_2 : tipo
        Segundo tipo del segundo Pokémon.
    tipo_a_3 : tipo
        Primer tipo del tercer Pokémon.
    tipo_b_3 : tipo
        Segundo tipo del tercer Pokémon.
    """
    deb_1, doble_deb_1, res_1, doble_res_1 = relacion(tipo_a_1, tipo_b_1)
    deb_2, doble_deb_2, res_2, doble_res_2 = relacion(tipo_a_2, tipo_b_2)
    deb_3, doble_deb_3, res_3, doble_res_3 = relacion(tipo_a_3, tipo_b_3)
    doble_deb = doble_deb_1 + doble_deb_2 + doble_deb_3
    if len(doble_deb) != 0:
        print('Existen ' + str(len(doble_deb)) + ' doble(s) debilidad(es): ' + str([i.nombre for i in doble_deb]))
    else:
        print('No existen doble debilidades.')
    
    deb = deb_1 + deb_2 + deb_3 + doble_deb_1 + doble_deb_2 + doble_deb_3
    for i in set(deb):
        if deb.count(i) > 1:
            print(str(deb.count(i)) + ' Pokémon tiene(n) debilidad a ' + i.nombre + '.')
    deb = set(deb)
    res = set(res_1 + res_2 + res_3 + doble_res_1 + doble_res_2 + doble_res_3)
    
    t = tipos.copy()
    for ti in res:
        t.remove(ti)
    for ti in deb:
        if ti in t:
            t.remove(ti)
    
    aux = deb.copy()
    for i in deb:
        if i in res:
            aux.remove(i)
    print('El equpo tiene ' + str(len(aux)) + ' vulnerabilidades de tipo: ' + str([i.nombre for i in aux]))
    
    cub_1 = list(set(common(tipo_a_1.debilidades, tipo_b_1.resistencias) +                 common(tipo_b_1.debilidades, tipo_a_1.resistencias)))
    cub_2 = list(set(common(tipo_a_2.debilidades, tipo_b_2.resistencias) +                 common(tipo_b_2.debilidades, tipo_a_2.resistencias)))
    cub_3 = list(set(common(tipo_a_3.debilidades, tipo_b_3.resistencias) +                 common(tipo_b_3.debilidades, tipo_a_3.resistencias)))
    cub = list(set(cub_1 + cub_2 + cub_3))
    cuby = []
    for i in cub:
        if i not in deb:
            if i not in res:
                if i not in t:
                    cuby.append(i)

    print('El equipo no es ni débil ni resistente a los tipos: ' + str([i.nombre for i in (t + cuby)]))


def tripleta(tipo_a_1, tipo_b_1, tipo_a_2, tipo_b_2, tipo_a_3, tipo_b_3):
    """Calcula indicadores sobre la resistencia de tipo del equipo
    
    Parameters
    ----------
    tipo_a_1 : tipo
        Primer tipo del primer Pokémon.
    tipo_b_1 : tipo
        Segundo tipo del primer Pokémon.
    tipo_a_2 : tipo
        Primer tipo del segundo Pokémon.
    tipo_b_2 : tipo
        Segundo tipo del segundo Pokémon.
    tipo_a_3 : tipo
        Primer tipo del tercer Pokémon.
    tipo_b_3 : tipo
        Segundo tipo del tercer Pokémon.
               
    Returns
    -------
    num_deb : int
        Número de vulnerabilidades no cubiertas por el equipo.
    num_doble_deb: int
        Número de doble debilidades del equipo.
    num_misma_deb: int
        Número de debilidades repetidas en más de un Pokémon.
    """
    deb_1, doble_deb_1, res_1, doble_res_1 = relacion(tipo_a_1, tipo_b_1)
    deb_2, doble_deb_2, res_2, doble_res_2 = relacion(tipo_a_2, tipo_b_2)
    deb_3, doble_deb_3, res_3, doble_res_3 = relacion(tipo_a_3, tipo_b_3)
    doble_deb = doble_deb_1 + doble_deb_2 + doble_deb_3
    
    num_doble_deb = len(set(doble_deb))
    
    deb = deb_1 + deb_2 + deb_3 + doble_deb_1 + doble_deb_2 + doble_deb_3
    num_misma_deb = 0
    for i in set(deb):
        if deb.count(i) > 1:
            num_misma_deb += 1
    deb = set(deb)
    res = set(res_1 + res_2 + res_3 + doble_res_1 + doble_res_2 + doble_res_3)
    
    aux = deb.copy()
    for i in deb:
        if i in res:
            aux.remove(i)
    num_deb = len(aux)
    return num_deb, num_doble_deb, num_misma_deb


def is_eq(l1, l2):
    l2_n = l2.copy()
    for i in l1:
        if i in l2_n:
            l2_n.remove(i)
    if len(l2_n) == 0:
        return True
    else:
        return False
    
def is_eq_complex(l1, l2):
    if not is_eq(l1, l2):
        return False
    else:
        l1_a = [l1[0], l1[1]]
        l1_b = [l1[2], l1[3]]
        l2_a = [l2[0], l2[1]]
        l2_b = [l2[2], l2[3]]
        if (is_eq(l1_a, l2_a) and is_eq(l1_b, l2_b)) or (is_eq(l1_a, l2_b) and is_eq(l1_b, l2_a)):
            return True
        else:
            return False

def info(tipo1, tipo2):
    """Muestra información de tipo de una combinación pokémon por     pantalla (si el pokémon no es doble tipo, ingresar dos veces su tipo).
    
    Parameters
    ----------
    tipo_1 : tipo
        Primer tipo del primer Pokémon.
    tipo_2 : tipo
        Segundo tipo del primer Pokémon.
    """
    deb, doble_deb, res, doble_res = relacion(tipo1, tipo2)
    print('Débil frente a :' + str([i.nombre for i in deb]))
    print('Doblemente débil frente a :' + str([i.nombre for i in doble_deb]))
    print('Resistente frente a :' + str([i.nombre for i in res]))
    print('Doblemente resistente frente a :' + str([i.nombre for i in doble_res]))

def buscador1(tipo1, tipo2, num_deb_max, num_doble_deb_max, num_misma_deb_max):
    """Busca dos combinaciones de tipo que cumpla las condiciones indicadas,     dada una combinación de tipo previa.
    
    Parameters
    ----------
    tipo1 : tipo
        Primer tipo del primer Pokémon.
    tipo2 : tipo
        Segundo tipo del primer Pokémon.
    num_deb_max : int
        Número de vulnerabilidades máximas no cubiertas máximas aceptadas para el equipo.
    num_doble_deb_max: int
        Número de doble debilidades máximas aceptadas para del equipo.
    num_misma_deb_max: int
        Número de debilidades repetidas máximas aceptadas en el equipo.
    """
    aux = []
    for tipo_a in tipos:
        for tipo_b in tipos:
            for tipo_c in tipos:
                for tipo_d in tipos:
                    num_deb, num_doble_deb, num_misma_deb = tripleta(tipo1, tipo2, tipo_a, tipo_b, tipo_c, tipo_d)
                    #Condición: número máximo de vulnerabilidades
                    if num_deb <= num_deb_max:
                        #Condición: número máximo de doble debilidades
                        if num_doble_deb <= num_doble_deb_max:
                            #Condición: número máximo de debilidades repetidas en el equipo
                            if num_misma_deb <= num_misma_deb_max:
                                aux.append([tipo_a, tipo_b, tipo_c, tipo_d])
    aux_2 = []
    if len(aux) == 0:
        print('No se han encontrado resultados.')
        return
    aux_2.append(aux[0])
    for i in aux:
        n = True
        for j in aux_2:
            if is_eq_complex(i, j):
                n = False
        if n == True:
            aux_2.append(i)
    print('Se han encontrado ' + str(len(aux_2)) + ' combinaciones diferentes: ')
    for i in aux_2:
        mos = [j.nombre for j in i]
        if mos[0] == mos[1] and mos[2] != mos[3]:
            print(mos[0] + ' & ' + mos[2] + ' / ' + mos[3])
        elif mos[0] != mos[1] and mos[2] == mos[3]:
            print(mos[2] + ' & ' + mos[0] + ' / ' + mos[1])
        elif mos[0] == mos[1] and mos[2] == mos[3]:
            print(mos[0] + ' & ' + mos[2])
        else:
            print(mos[0] + ' / ' + mos[1] + ' & ' + mos[2] + ' / ' + mos[3])


def buscador2(tipo1, tipo2, tipo3, tipo4, num_deb_max, num_doble_deb_max, num_misma_deb_max):
    """Busca una combinación de tipos que cumpla las condiciones indicadas,     dadas dos combinaciones de tipo previas.
    
    Parameters
    ----------
    tipo1 : tipo
        Primer tipo del primer Pokémon.
    tipo2 : tipo
        Segundo tipo del primer Pokémon.
    tipo3 : tipo
        Primer tipo del segundo Pokémon.
    tipo4 : tipo
        Segundo tipo del segundo Pokémon.
    num_deb_max : int
        Número de vulnerabilidades máximas no cubiertas máximas aceptadas para el equipo.
    num_doble_deb_max: int
        Número de doble debilidades máximas aceptadas para del equipo.
    num_misma_deb_max: int
        Número de debilidades repetidas máximas aceptadas en el equipo.
    """
        
    aux = []
    for tipo_a in tipos:
        for tipo_b in tipos:
            num_deb, num_doble_deb, num_misma_deb = tripleta(tipo1, tipo2, tipo3, tipo4, tipo_a, tipo_b)
            #Condición: número máximo de vunerabilidades
            if num_deb <= num_deb_max:
                #Condición: número máximo de doble debilidades
                if num_doble_deb <= num_doble_deb_max:
                    #Condición: número máximo de debilidades repetidas en el equipo
                    if num_misma_deb <= num_misma_deb_max:
                        aux.append([tipo_a, tipo_b])
    aux_2 = []
    if len(aux) == 0:
        print('No se han encontrado resultados.')
        return
    aux_2.append(aux[0])

    for i in aux:
        n = True
        for j in aux_2:
            if is_eq(i, j):
                n = False
        if n == True:
            aux_2.append(i)  
    print('Se han encontrado ' + str(len(aux_2)) + ' combinaciones diferentes: ')
    for i in aux_2:
        mos = [j.nombre for j in i]
        if mos[0] == mos[1]:
            print(mos[0])
        else:
            print(mos[0] + ' / ' + mos[1])

