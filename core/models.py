from django.db import models

from django.db import models

from stdimage.models  import StdImageField


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class ProdutosModel(Base):
    ICONE = ('best_box','Caixa'),

    nome = models.CharField('Nome', max_length=100)
    modelo = models.CharField('Fabricante', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('icone', max_length=13, choices=ICONE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome
