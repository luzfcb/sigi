from django.contrib.auth.admin import Group, GroupAdmin, User, UserAdmin
from django.contrib.sites.admin import Site, SiteAdmin
from django.contrib.admin.sites import AdminSite
from maintenancemode.admin import AllowedPath, AllowedPathAdmin
from sigi.apps.casas.admin import CasaLegislativa, CasaLegislativaAdmin
from sigi.apps.contatos.admin import (UnidadeFederativa, UnidadeFederativaAdmin,
                                      Municipio, MunicipioAdmin, Telefone,
                                      TelefoneAdmin, Contato, ContatoAdmin)
from sigi.apps.convenios.admin import (Convenio, ConvenioAdmin, EquipamentoPrevisto,
                                       EquipamentoPrevistoAdmin, Anexo, AnexoAdmin)
from sigi.apps.inventario.admin import (Fornecedor, FornecedorAdmin, Fabricante,
                                        FabricanteAdmin, Equipamento,
                                        EquipamentoAdmin, TipoEquipamento,
                                        TipoEquipamentoAdmin, ModeloEquipamento,
                                        ModeloEquipamentoAdmin, Bem, BemAdmin)
from sigi.apps.servicos.admin import Servico, ServicoAdmin
from sigi.apps.mesas.admin import (Legislatura, LegislaturaAdmin, Coligacao,
                                   ColigacaoAdmin, ComposicaoColigacao,
                                   ComposicaoColigacaoAdmin, SessaoLegislativa,
                                   SessaoLegislativaAdmin, MesaDiretora,
                                   MesaDiretoraAdmin, Cargo, CargoAdmin,
                                   MembroMesaDiretora, MembroMesaDiretoraAdmin)
from sigi.apps.parlamentares.admin import (Partido, PartidoAdmin, Parlamentar,
                                           ParlamentarAdmin, Mandato, MandatoAdmin)

class  DefaultSite(AdminSite):
    index_template = 'index.html'
    login_template = 'login.html'

default = DefaultSite()

# django.contrib.auth
default.register(Group, GroupAdmin)
default.register(User, UserAdmin)

# django.contrib.sites
default.register(Site, SiteAdmin)

# maintenancemode
default.register(AllowedPath, AllowedPathAdmin)

# sigi.apps.casas
default.register(CasaLegislativa, CasaLegislativaAdmin)

# sigi.apps.contatos
default.register(UnidadeFederativa, UnidadeFederativaAdmin)
default.register(Municipio, MunicipioAdmin)
default.register(Telefone, TelefoneAdmin)
default.register(Contato, ContatoAdmin)

# sigi.apps.convenios
default.register(Convenio, ConvenioAdmin)
default.register(EquipamentoPrevisto, EquipamentoPrevistoAdmin)
default.register(Anexo, AnexoAdmin)

# sigi.apps.inventario
default.register(Fornecedor, FornecedorAdmin)
default.register(Fabricante, FabricanteAdmin)
default.register(TipoEquipamento, TipoEquipamentoAdmin)
default.register(ModeloEquipamento,ModeloEquipamentoAdmin)
default.register(Equipamento, EquipamentoAdmin)
default.register(Bem, BemAdmin)

# sigi.apps.servicos
default.register(Servico, ServicoAdmin)

# sigi.apps.mesas
default.register(Legislatura, LegislaturaAdmin)
default.register(Coligacao, ColigacaoAdmin)
default.register(ComposicaoColigacao, ComposicaoColigacaoAdmin)
default.register(SessaoLegislativa, SessaoLegislativaAdmin)
default.register(MesaDiretora, MesaDiretoraAdmin)
default.register(Cargo, CargoAdmin)
default.register(MembroMesaDiretora, MembroMesaDiretoraAdmin)

# sigi.apps.parlamentares
default.register(Partido, PartidoAdmin)
default.register(Parlamentar, ParlamentarAdmin)
default.register(Mandato, MandatoAdmin)