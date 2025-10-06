from django.db import models
from django.core.validators import MaxLengthValidator


class Film(models.Model):
    """Модель для фильмов"""
    title = models.CharField(
        max_length=200, 
        verbose_name="Название фильма",
        validators=[MaxLengthValidator(200)]
    )
    description = models.CharField(
        max_length=250, 
        verbose_name="Описание фильма",
        validators=[MaxLengthValidator(250)]
    )
    review_text = models.TextField(verbose_name="Отзыв")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Фильм '{self.title}'"
    
    def get_short_description(self):
        """Возвращает сокращенное описание фильма"""
        if len(self.description) > 100:
            return self.description[:100] + "..."
        return self.description
    
    def get_short_review(self):
        """Возвращает сокращенный отзыв"""
        if len(self.review_text) > 200:
            return self.review_text[:200] + "..."
        return self.review_text