from datetime import date

from pydantic import conint

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


def get_tipos_documento():
    """OBTENER TIPOS DE DOCUMENTOS"""
    return _get("tipodocs")


def post_dte(
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


def get_dte(
    tipodoc: TipoDocumento,
    folio: NumeroFolio,
    expects: Optional[ExpectsDTE],
) -> ResponseDTE:
    """CONSULTA DE DOCUMENTOS"""
    params = {"tipodoc": tipodoc, "folio": folio}
    if expects:
        params["expects"] = expects
    return _get("dtes", params=params)


def post_boleta(
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


def get_boleta(
    tipodoc: TipoDocumento, folio: NumeroFolio, expects: Optional[ExpectsDTE]
):
    """CONSULTA DE BOLETAS"""
    params = {"tipodoc": tipodoc, "folio": folio}
    if expects:
        params["expects"] = expects
    return _get("boletas", params=params)


def get_documentos_recibidos(
    received_on: Optional[date],
    issued_on: Optional[date],
    results_per_page: conint(ge=1, le=100) = 10,
    page: int = 1,
):
    """CONSULTA DE DOCUMENTOS RECIBIDOS"""
    params = {
        "rpp": results_per_page,
        "page": page,
    }
    if received_on:
        params["fecharecepcion"] = received_on.strftime("%Y-%m-%d")
    if issued_on:
        params["fechaemision"] = issued_on.strftime("%Y-%m-%d")
    return _get("recepciondtes", params=params)
