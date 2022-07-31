from lioren.core import _get



def get_my_company():
    """ OBTENCIÓN DE DATOS DE LA EMPRESA """
    return _get('miempresa')


def get_regions():
    """ OBTENCIÓN DE REGIONES SII """
    return _get('regiones')


def get_counties(region_id=None):
    """ OBTENCIÓN DE COMUNAS SII """
    if region_id is None:
        return _get('comunas')
    else:
        return _get('comunas', params={'region_id':region_id})


def get_cities(region_id=None):
    """ OBTENCIÓN DE CIUDADES SII """
    if region_id is None:
        return _get('ciudades')
    else:
        return _get('ciudades', params={'region_id':region_id})


def get_payment_methods():
    """ OBTENCIÓN DE MEDIOS DE PAGO """
    return _get('mediopagos')


def get_reference_reasons():
    """ OBTENCIÓN DE RAZONES DE REFERENCIA """
    return _get('razonesref')


def get_shipping_types():
    """ OBTENCIÓN DE TIPOS DE DESPACHO """
    return _get('tipodespachos')


def get_transfer_types():
    """ OBTENCIÓN DE TIPOS DE TRASLADO """
    return _get('tipotraslados')


def get_branch_offices():
    """ OBTENCIÓN DE SUCURSALES """
    return _get('sucursales')
