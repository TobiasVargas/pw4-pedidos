from django.db import models


class Categoria(models.Model):

    nome = models.CharField(max_length=30, verbose_name="Nome")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Produto(models.Model):

    LITROS = "L"
    GRAMAS = "GR"
    KILOS = "KG"
    UNIDADE = "UN"
    PECA = "PC"

    UNIDADES = [
        (LITROS, "Litros"),
        (GRAMAS, "Gramas"),
        (KILOS, "Kilos"),
        (UNIDADE, "Unidade"),
        (PECA, "Peça")
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    categoria = models.ForeignKey("produtos.Categoria", verbose_name="categoria", on_delete=models.CASCADE)
    unidade = models.CharField(max_length=2, choices=UNIDADES)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome
