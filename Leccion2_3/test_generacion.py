import pytest


def generacion():
    """
    Funcion que permite identificar la generación a la cual perteneces según el año de nacimiento
    
    Usage:
    
    >>>Hace algo
    >>>Hace otra cosa
    
    """
    anio = 1956
    
    if anio >= 1930 and anio <= 1948:
        return "Generacion Silenciosa"
    elif anio >= 1948 and anio <= 1968:
        return "Baby Boom"
    elif anio >= 1969 and anio <= 1980:
        return "Generacion X"
    elif anio >= 1981 and anio <= 1993:
        return "Millenials"        
    elif anio >= 1994 and anio <= 2010:
        return "Generacion Z"
    elif anio >= 2010:
        return "Debe tener mas de 12 años para participar"
    else:
        return "Generacion invalida"
    
def test_generacionSilenciosa():
    """
    Cuando el año ingresado se encuentre entre 1930 y 1948, la generación será: Silenciosa"
    '"""   
    assert generacion() == "Generacion Silenciosa","Año debe estar entre 1930 y 1948"

def test_generacionBabyBoom():
    """
    Cuando el año ingresado se encuentre entre 1948 y 1968, la generación será: Baby Boom"
    """ 
    assert generacion() == "Baby Boom","Año debe estar entre 1948 y 1968"
    
def test_generacionX():
    '''
    Cuando el año ingresado se encuentre entre 1969 y 1980, la generación será: X"
    '''     
    assert generacion() == "Generacion X","Año debe estar entre 1969 y 1980"

def test_generacionMillenials():
    '''
    Cuando el año ingresado se encuentre entre 1981 y 1993, la generación será: Milenials"
    ''' 
    assert generacion() == "Millenials","Año debe estar entre 1981 y 1993"

def test_generacionZ():
    '''
    Cuando el año ingresado se encuentre entre 1930 y 1948, la generación será: Z"
    ''' 
    assert generacion() == "Generacion Z","Año debe estar entre 1994 y 2010"

