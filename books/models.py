from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя категории")
    adult = models.BooleanField(default=False, verbose_name="Ограничение для взрослых")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Book(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    author = models.CharField(max_length=200, verbose_name="Имя автора")
    poster = models.ImageField(verbose_name="Обложка", upload_to="covers/", blank=True, default="default.jpg")
    category = models.ManyToManyField(Category, verbose_name="Категория", related_name="categories")
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.name} - {self.author}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
