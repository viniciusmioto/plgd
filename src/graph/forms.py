from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


MODEL_CHOICES = (
    ("#1", 'KNN'),
    ("#2", 'SVM'),
    ("#3", 'RAND_FOREST'),
    ("#4", 'GRAD_BOOSTING')
)

class ModelsForm(forms.Form):
    model_type = forms.ChoiceField(choices=MODEL_CHOICES)
    graph_file = forms.FileField()