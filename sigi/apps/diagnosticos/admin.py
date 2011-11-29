# -*- coding: utf-8 -*-
from django.contrib import admin
from eav.admin import BaseEntityAdmin, BaseSchemaAdmin
from sigi.apps.diagnosticos.models import Diagnostico, Pergunta, Escolha, Equipe, Anexo, Categoria
from sigi.apps.diagnosticos.forms import DiagnosticoForm


"""
Actions do Admin
"""


# Ação de alterar o status das publicações no modo Draft para Publicado.
def alterar_status_publicacao(self, request, queryset):
    for registro in queryset:
        diagnostico = Diagnostico.objects.get(pk=registro.id)
        diagnostico.status = True
        diagnostico.save()

        # Enviando o email avisando que o diagnóstico foi publicado
        diagnostico.email_diagnostico_publicado(diagnostico.responsavel.email_pessoal, request.get_host())
    self.message_user(request, "Diagnóstico(s) publicado(s) com sucesso!")
alterar_status_publicacao.short_description = u"""
    Definir diagnósticos como publicado"""


# Ação de alterar o status das publicações no modo Publicado para Draft.
def alterar_status_draft(self, request, queryset):
    queryset.update(status=False)
alterar_status_draft.short_description = u"""
    Definir diagnósticos como não publicado"""


class EquipeInline(admin.TabularInline):
    model = Equipe
    extra = 4


class AnexosInline(admin.TabularInline):
    model = Anexo
    extra = 2
    exclude = ['data_pub', ]


class AnexoAdmin(admin.ModelAdmin):
    date_hierarchy = 'data_pub'
    exclude = ['data_pub', ]
    list_display = ('arquivo', 'descricao', 'data_pub', 'diagnostico')
    raw_id_fields = ('diagnostico',)
    search_fields = ('descricao', 'diagnostico__id', 'arquivo',
                     'diagnostico__casa_legislativa__nome')


class DiagnosticoAdmin(BaseEntityAdmin):
    form = DiagnosticoForm
    date_hierarchy = 'data_questionario'
    actions = [alterar_status_publicacao, alterar_status_draft]
    inlines = (EquipeInline, AnexosInline)
    list_display = ('casa_legislativa', 'data_questionario', 'status')
    raw_id_fields = ('casa_legislativa', 'responsavel')

    eav_fieldsets = [
        (u'00. Identificação do Diagnóstico', {'fields': ('responsavel', 'data_visita', 'data_questionario', 'data_relatorio_questionario')}),
        (u'01. Identificação da Casa Legislativa', {'fields': ('casa_legislativa',)}),
        (u'02. Identificação de Competências da Casa Legislativa', {'fields': ()})
      ]

    # popula o eav fieldsets ordenando as categorias e as perguntas
    # para serem exibidas no admin
    for categoria in Categoria.objects.all():
        # ordena as perguntas pelo title e utiliza o name no fieldset
        perguntas_by_title = [(p.title, p.name) for p in categoria.perguntas.all()]
        perguntas = [pergunta[1] for pergunta in sorted(perguntas_by_title)]

        eav_fieldsets.append((categoria, {
          'fields': tuple(perguntas),
          'classes': ['collapse']
          }))


class PerguntaAdmin (BaseSchemaAdmin):
    search_fields = ('title', 'help_text', 'name',)
    list_display = ('title', 'categoria', 'datatype', 'help_text', 'required')
    list_filter = ('datatype', 'categoria', 'required')


class EscolhaAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'schema', 'schema_to_open')
    raw_id_fields = ('schema', 'schema_to_open')
    ordering = ('schema', 'title')

admin.site.register(Diagnostico, DiagnosticoAdmin)
admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Escolha, EscolhaAdmin)
admin.site.register(Anexo, AnexoAdmin)
admin.site.register(Categoria)