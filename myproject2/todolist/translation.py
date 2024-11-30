from .models import Task, Category
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Task)
class TaskTranslationOptions(TranslationOptions):
    fields = ('task_name', 'description')