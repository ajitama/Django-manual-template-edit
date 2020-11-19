from django.shortcuts import render
from django.views.generic import CreateView
from .models import TestMaster
from .forms import TestMasterModelForm



# Create your views here.
class TestMasterCreateView(CreateView):

    # 新規登録
    template_name = 'formman/form.html'
    form_class = TestMasterModelForm # 扱う項目の定義をCouponFormで指定
    model = TestMaster # 扱うモデル(テーブル)

    def get(self, request, *args, **kwargs):
        #print(self.form_class)
        return super().get(self, request, *args, **kwargs)

