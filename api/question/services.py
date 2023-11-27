from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import QuestionsBase


# def duplicate_questions_base(request, questions_base_id):
#     original_questions_base = get_object_or_404(QuestionsBase, pk=questions_base_id)
#
#     # Создание копии
#     duplicate_questions_base = QuestionsBase.objects.create(
#         subject=original_questions_base.subject,  # Скопировать связанный объект subject
#         title=f"Copy of {original_questions_base.title}"  # Создать название для копии
#         # Здесь скопируйте другие поля, если они есть
#     )
#
#     # Возврат нового дубликата в формате JSON
#     return Response({"id": duplicate_questions_base.id, "title": duplicate_questions_base.title})