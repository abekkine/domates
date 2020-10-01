# -*- coding : utf-8 -*-

from django.db import models

class DocumentMaster(models.Model):
    def __str__(self):
        return "%s [%s]" % (self.title, self.prefix)

    title = models.CharField(max_length=256)
    prefix = models.CharField(max_length=16)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now = True)

class DocumentRow(models.Model):
    def __str__(self):
        return self.text

    class DocumentRowKind(models.TextChoices):
        HEADER      = 'HD', 'Header'
        PARAGRAPH   = 'PR', 'Paragraph'
        FIGURE      = 'FG', 'Figure'
        TABLE       = 'TB', 'Table'

    kind = models.CharField(
        max_length=2,
        choices = DocumentRowKind.choices,
        default = DocumentRowKind.PARAGRAPH,
    )
    master = models.ForeignKey(DocumentMaster, on_delete=models.CASCADE)
    uid = models.IntegerField(blank=True, null=True)
    text = models.TextField()
    before = models.ForeignKey('self', blank=True, null=True, related_name='row_before', on_delete=models.SET_NULL)
    above = models.ForeignKey('self', blank=True, null=True, related_name='row_above', on_delete=models.SET_NULL)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now = True)