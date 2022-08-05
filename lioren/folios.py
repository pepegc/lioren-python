from lioren.core import _get
from lioren.core import _post


def get_caf(type, results_per_page=10, page=1):
    """INDICE DE CODIGOS DE AUTORIZACION DE FOLIOS (CAFs)
    Keyword arguments:
    type -- String (minlength 2, maxlength 3)
    results_per_page -- Integer (min 1, max 100)
    page -- Integer (min 1)
    """
    params = {"tipodoc": type, "rpp": resuls_per_page, "page": page}
    return _get("cafs", params=params)


def get_caf(id):
    """CONSULTA DE CODIGOS DE AUTORIZACION DE FOLIOS (CAFs)
    Keyword arguments:
    id -- Integer (min 1, max 100)
    """
    return _get("cafs/" + str(id))


def post_caf(type, quantity):
    """EMISION DE CODIGOS DE AUTORIZACION DE FOLIOS (CAF)
    Keyword arguments:
    type -- String (minlength 2, maxlength 3)
    quantity -- Integer (min 1, max 10000)
    """
    data = {"tipodoc": type, "quantity": quantity}
    return _post("cafs", data=data)


def get_number(type, number):
    """CONSULTA DE FOLIO
    Keyword arguments:
    type -- String (minlength 2, maxlength 3)
    number -- Integer (min 1, max 10000)
    """
    params = {"tipodoc": type, "folio": number}
    return _get("folios", params=params)
