# encoding=utf-8

from django.db import models

class Todo(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "ToDo"
        ordering = ("id", )

    name = models.CharField("タイトル",max_length=100)
    description = models.TextField("詳細", blank=True)
    created_at = models.DateTimeField("登録日", auto_now_add=True)
    finished_at = models.DateTimeField("完了日", blank=True, null=True)
