from lioren.core import _get
from lioren.core import _post
from lioren.schemas import (
    EmisorDTE,
    ReceptorDTE,
    DetalleDTE,
    PagoDTE,
    ReferenciaDTE,
    ExpectsDTE,
    ResponseDTE,
)


def get_document_types():
    """OBTENCIÓN DE TIPOS DE DOCUMENTOS"""
    return _get("tipodocs")


def post_document(
    emisor: EmisorDTE,
    receptor: ReceptorDTE,
    detalles: list[DetalleDTE],
    pagos: Optional[list[PagoDTE]],
    referencias: Optional[list[ReferenciaDTE]],
    expects: Optional[ExpectsDTE],
) -> ResponseDTE:
    """EMITIR DOCUMENTO TRIBUTARIO ELECTRONICO"""
    data = {"emisor": emisor, "receptor": receptor, "detalles": detalles}
    if pagos:
        data["pagos"] = pagos
    if referencias:
        data["referencias"] = referencias
    if expects:
        data["expects"] = expects
    return _post("dtes", data=data)


def get_document(
    tipodoc: TipoDocumento,
    folio: NumeroFolio,
    expects: Optional[ExpectsDTE],
) -> ResponseDTE:
    """CONSULTA DE DOCUMENTOS"""
    params = {"tipodoc": tipodoc, "folio": folio}
    if expects is not None:
        params["expects"] = expects
    return _get("dtes", params=params)


def post_receipt(
    detalles, emisor, receptor=None, pagos=None, referencias=None, expects=None
):
    """EMITIR BOLETA ELECTRONICA"""
    data = {"emisor": emisor, "detalles": detalles}
    if receptor:
        data["receptor"] = receptor
    if pagos:
        data["pagos"] = pagos
    if referencias:
        data["referencias"] = referencias
    if expects:
        data["expects"] = expects
    return _post("boletas", data=data)


def get_receipt(type, number, expects=None):
    """CONSULTA DE BOLETAS
    Keyword arguments:
    type -- String (minlength 2, maxlength 3)
    number -- Integer (min 1, max 999999999)
    expects -- String (xml | pdf)
    """
    params = {"tipodoc": type, "folio": number}
    if expects is not None:
        params["expects"] = expects
    return _get("boletas", params=params)


def get_received_documents(received_on=None, issued_on=None, rpp=10, page=1):
    """CONSULTA DE DOCUMENTOS RECIBIDOS
    Keyword arguments:
    received_on -- String (YYYY-MM-DD)
    issued_on -- String (YYYY-MM-DD)
    results_per_page -- Integer (min 1, max 100)
    page -- Integer (min 1)
    """
    params = {
        "fecharecepcion": received_on,
        "fechaemision": issued_on,
        "rpp": rpp,
        "page": page,
    }
    return _get("recepciondtes", params=params)
