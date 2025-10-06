from django import forms
from .models import Film


class FilmForm(forms.ModelForm):
    """Форма для создания и редактирования фильмов"""
    
    class Meta:
        model = Film
        fields = ['title', 'description', 'review_text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название фильма',
                'maxlength': '200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание фильма',
                'rows': 3,
                'maxlength': '250'
            }),
            'review_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш отзыв о фильме',
                'rows': 6
            })
        }
        labels = {
            'title': 'Название фильма',
            'description': 'Описание фильма',
            'review_text': 'Ваш отзыв'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем Bootstrap классы для всех полей
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
    
    def clean_title(self):
        """Валидация названия фильма"""
        title = self.cleaned_data.get('title')
        if not title or len(title.strip()) < 2:
            raise forms.ValidationError("Название фильма должно содержать минимум 2 символа")
        return title.strip()
    
    def clean_description(self):
        """Валидация описания фильма"""
        description = self.cleaned_data.get('description')
        if not description or len(description.strip()) < 10:
            raise forms.ValidationError("Описание фильма должно содержать минимум 10 символов")
        return description.strip()
    
    def clean_review_text(self):
        """Валидация текста отзыва"""
        review_text = self.cleaned_data.get('review_text')
        if not review_text or len(review_text.strip()) < 20:
            raise forms.ValidationError("Отзыв должен содержать минимум 20 символов")
        return review_text.strip()
