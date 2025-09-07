from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="категория",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="продукт", help_text="Введите наименование продукта"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="описание продукта"
    )
    photo = models.ImageField(
        upload_to="catalog/photo", blank=True, null=True, verbose_name="фото"
    )
    categor = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="категория",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField()
    created_at = models.DateField(blank=True, null=True, verbose_name="дата создания")
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="дата последнего изменения"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "categor", "price"]

    def __str__(self):
        return self.name
