from django import forms
from .models import TestMaster

class TestMasterModelForm(forms.ModelForm):
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # formを開いた際の属性変更など。
        #self.fields['security_key'].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = TestMaster
        fields = '__all__'
        #fields = [
        #        'qrid',
        #        'pos_item_code',
        #        'security_key',
        #        ]
