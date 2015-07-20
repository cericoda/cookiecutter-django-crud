from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}Form(forms.ModelForm):
    class Meta:
        model = {{ cookiecutter.model_name }}

    def __init__(self, *args, **kwargs):
        super({{ cookiecutter.model_name }}Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.form_id = 'id-{{ cookiecutter.model_name|lower }}-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
#         self.helper.form_method = 'post'
#         self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
        
#         self.helper.form_tag = False
#         self.helper.form_class = 'form-horizontal'
#         self.helper.label_class = 'col-lg-2'
#         self.helper.field_class = 'col-lg-8'


#         self.helper.layout = Layout(Field('id', type="hidden"),
#                                     Div(
#                               Div(
#                                   Div(Field('name', css_class='input-medium'), css_class='span2'),
#                                   Div(Field('status', css_class='input-medium'), css_class='span2'),
#                               Div(
#                                   Div(Field('instructions', css_class='span10 ckeditor'), css_class='span9'),
#                                   css_class='row-fluid'), 
#                                 ),)
#         client_id = kwargs.pop('client_id', None)
#         self.fields['client_lead_project_contact'].queryset = Contact.objects.active().filter(client=client)
#         self.fields['client'].widget=HiddenInput()
#         self.fields['details'].widget=Textarea()
#         self.fields['quote_prepared_by'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
#         self.fields['project_deadline'].required = True

