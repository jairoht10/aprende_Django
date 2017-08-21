from django.utils.translation import ugettext_lazy as _

## Mensaje de error para peticiones AJAX
MSG_NOT_AJAX = _("No se puede procesar la petición. "
                 "Verifique que posea las opciones javascript habilitadas e intente nuevamente.")

TIPO_FRENTE = (
    ("JC",_("Jefe del Comando Zamora 200")),
    ("GC",_("Gobierno de Calle Constituyente")),
    ("OE",_("Organización y Estructura de la Maquinaria Electoral")),
    ("EP",_("Estrategia y Propaganda")),
    ("MP",_("Movilización Permanente")),
    ("FM",_("Frente de Movimientos Sociales Constituyentes")),
)

SHORT_NACIONALIDAD = (
    ("V", "V"), ("E", "E")
)
