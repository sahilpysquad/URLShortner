from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from url_shortner.forms import URLShortnerModelForm, VerifyPasswordForm
from url_shortner.models import URLShortner


class URLShortnerCreateView(View):
    template_name = 'url_shortner/home_page.html'
    form_class = URLShortnerModelForm
    success_url = '/url-shortner/'

    def get(self, request):
        objs = URLShortner.objects.all()
        return render(request=request, template_name=self.template_name,
                      context={'form': self.form_class(), 'objs': objs})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            new_url = form.instance.short_url
            return JsonResponse({'new_url': new_url})
        else:
            return redirect(self.success_url)


class VerifiedPasswordView(View):
    template_name = 'url_shortner/verify_password.html'
    form_class = VerifyPasswordForm
    model = URLShortner

    def get(self, request, short_url):
        return render(request=request, template_name=self.template_name, context={'form': self.form_class()})

    def post(self, request, short_url):
        obj = self.model.objects.filter(short_url=short_url).first()
        if obj:
            form = self.form_class(data=request.POST)
            if form.is_valid():
                password = form.cleaned_data.get('password')
                if not obj.check_password(raw_password=password):
                    return 'Invalid Password..!'
                long_url = obj.long_url
                return redirect(to=long_url)
            else:
                pass
        else:
            return "Invalid URL"
        return None
