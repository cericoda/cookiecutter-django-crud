from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from model_utils.models import StatusModel, TimeStampedModel
from model_utils.choices import Choices

class NonArchived{{ cookiecutter.model_name }}Manager(models.Manager):
    def get_query_set(self):
        return super(NonArchived{{ cookiecutter.model_name }}Manager, self).get_query_set().exclude(status='Archived')

@python_2_unicode_compatible
class {{ cookiecutter.model_name }}(StatusModel, TimeStampedModel):
    STATUS = Choices(('active', 'Active'), 
                     ('archived', 'Archived'),
                      )
    name = models.CharField(max_length=255)

    all{{ cookiecutter.model_name|lower}} = models.Manager() # Establish this as the default/automatic manager
    objects = NonArchived{{ cookiecutter.model_name }}Manager()

    def __str__(self):
        return '{{ cookiecutter.model_name }} ({})'.format(self.id or 'Unsaved')

    def get_absolute_url(self):
        return reverse('{{ cookiecutter.model_name|lower }}:detail', args=[str(self.id)])

