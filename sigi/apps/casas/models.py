# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from sigi.apps.mesas.models import MesaDiretora, MembroMesaDiretora
from sigi.apps.parlamentares.models import Parlamentar
from sigi.apps.utils import SearchField

class TipoCasaLegislativa(models.Model):
    sigla = models.CharField(
        max_length=5
    )
    nome = models.CharField(
        max_length=100
    )
    def __unicode__(self):
        return self.nome
    

class CasaLegislativa(models.Model):
    nome = models.CharField(
        max_length=60,
        help_text='Exemplo: <em>Câmara Municipal de Pains</em>.'
    )
    search_text = SearchField(field_names=['nome'])
    tipo = models.ForeignKey(TipoCasaLegislativa, verbose_name="Tipo")
    cnpj = models.CharField('CNPJ', max_length=32, blank=True)
    observacoes = models.TextField(u'observações', blank=True)
    presidente = models.CharField('Presidente', max_length=150, blank=True)

    logradouro = models.CharField(
        max_length=100,
        help_text='Avenida, rua, praça, jardim, parque...'
    )
    bairro = models.CharField(max_length=100, blank=True)
    municipio = models.ForeignKey(
        'contatos.Municipio',
        verbose_name='município'
    )
    municipio.uf_filter = True
    cep = models.CharField(max_length=32)
    email = models.EmailField('e-mail', max_length=128, blank=True)
    pagina_web = models.URLField(
        u'página web',
        help_text='Exemplo: <em>http://www.camarapains.mg.gov.br</em>.',
        blank=True,
        verify_exists=False
    )
    telefone = models.CharField('Telefone', max_length=100, blank=True)
    telefones = generic.GenericRelation('contatos.Telefone')

    foto = models.ImageField(
        upload_to='imagens/casas',
        width_field='foto_largura',
        height_field='foto_altura',
        blank=True
    )
    foto_largura = models.SmallIntegerField(editable=False, null=True)
    foto_altura = models.SmallIntegerField(editable=False, null=True)


    contatos = generic.GenericRelation('contatos.Contato')

    class Meta:
        ordering = ('nome',)
        unique_together = ('municipio', 'tipo')
        verbose_name = 'Casa Legislativa'
        verbose_name_plural = 'Casas Legislativas'

    def __unicode__(self):
        return self.nome

    def get_presidente_nome(self):
        try:
            mesa = MesaDiretora.objects.get(casa_legislativa=self)
            membro = mesa.membromesadiretora_set.get(
                cargo__descricao__iexact='presidente'
            )
        except (MesaDiretora.DoesNotExist, MembroMesaDiretora.DoesNotExist):
            return ''
        return membro.parlamentar.nome_completo
