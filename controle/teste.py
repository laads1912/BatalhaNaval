# import sys
# print(sys.path)

# '''from controlador_sistema import ControladorSistema
#
#
# ControladorSistema().inicializa_sistema()'''

from controlador_sistema import ControladorSistema
from controlador_partida import ControladorPartida

teste = ControladorPartida(ControladorSistema())
teste.add_embarcacoes()
