from enum import Enum
from pydantic import BaseModel, EmailStr, Optional
from datetime import date


Telefono = conint(ge=100000000, le=999999999)
RUT = str  # TODO

TipoDocumento = constr(min_length=2, max_length=3, strip_whitespace=True)
RazonSocial = constr(min_length=5, max_length=100, strip_whitespace=True)
Giro = constr(min_length=5, max_length=40, strip_whitespace=True)
Localidad = constr(min_length=3, max_length=20, strip_whitespace=True)
Direccion = constr(min_length=5, max_length=50, strip_whitespace=True)
Nombre = constr(min_length=5, max_length=80, strip_whitespace=True)

NumeroFolio = conint(
    ge=1, le=999999999999
)  # https://www.lioren.cl/docs#/api-consultadte


class EmisorDTE(BaseModel):
    tipodoc: TipoDocumento
    fecha: date
    actividad: Optional[int]
    sucursal: Optional[int]
    email: Optional[EmailStr]
    telefono: Optional[Telefono]
    tipodespacho: Optional[int]
    tipotraslado: Optional[int]


class ReceptorDTE(BaseModel):
    rut: RUT
    rs: RazonSocial
    giro: Giro
    comuna: int
    ciudad: int
    localidad: Optional[Localidad]
    direccion: str
    email: Optional[EmailStr]
    telefono: Optional[Telefono]
    nombresolicitante: Opcional[Nombre]
    rutsolicitante: Optional[RUT]


class DetalleDTE(BaseModel):
    codigo: Optional[constr(min_length=3, max_length=128, strip_whitespace=True)]
    nombre: Nombre
    cantidad: confloat(ge=0.000001, le=999999999)
    unidad: Optional[constr(min_length=2, max_length=4, strip_whitespace=True)]
    precio: confloat(ge=0, le=999999999)
    impuestoadicional: Optional[conint(ge=10, le=999)]
    montoimpuesto: Optional[conint(ge=10, le=999999999)]
    descuento: Optional[conint(ge=1, le=100)]
    descripcion: Optional[constr(max_length=1000, strip_whitespace=True)]
    exento: bool
    bodega: Optional[int]


class PagoDTE(BaseModel):
    fecha: date
    mediopago: int
    glosa: Optional[constr(max_length=40, strip_whitespace=True)]
    cobrar: bool


class ReferenciaDTE(BaseModel):
    fecha: date
    tipodoc: TipoDocumento
    folio: constr(min_length=1, max_length=18, strip_whitespace=True)
    razon: int
    glosa: constr(min_length=5, max_length=80, strip_whitespace=True)


class ExpectsDTE(str, Enum):
    xml = "xml"
    pdf = "pdf"
    _all = "all"


class DTEResponse(BaserModel):
    id: int
    tipodoc: TipoDocumento
    folio: int
    fecha: str
    rut: str
    rs: str
    montoneto: int
    montoexento: int
    montoiva: int
    montototal: int
    detalles: list
    pagos: list
    referencias: list
    pdf: str
    xml: str
    estado: str
    glosaestado: Optional[str]
    trackid: Optional[str]
    errors: Optional[list]
