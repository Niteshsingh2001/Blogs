
from django import forms
from .models import Article


class articles_form(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['tittle',"content"]


    def clean(self):
        data = self.cleaned_data
        t = data.get("tittle")
        q = Article.objects.filter(tittle__icontains=t)
        if q.exists():
            self.add_error("tittle","already exists")
        return data
 

class articles_formold(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data #dict
        title = cleaned_data.get('title')
        cont = cleaned_data.get('content')
        if title == "xyz":
            raise self.add_error('title',"xyz")

        if cont == '123':
            raise self.add_error('cont',"420")
        print(title)
        return title