from django.shortcuts import render
from .forms import SimpleForm
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Rating
from .forms import RegisterForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy


@method_decorator(login_required, name="dispatch")
class RatingsDetailView(DetailView):
    model = Rating

class RatingsListView(ListView):
    model = Rating
    paginate_by = 2
    context_object_name = "kostya_ispolzyu_norm_imena"
    

class RatingsEntryListView(ListView):
    template_name = "rating/rating_by_name.html"
    context_object_name = "rating_name_objects"

    def get_queryset(self):
        return Rating.objects.filter(name=self.kwargs["name"])


@method_decorator(login_required, name="dispatch")
class SimpleView(View):
    def get(self, request) :
        return HttpResponse("hello world")

class SimpleFormView(View):
    form_class = SimpleForm
    initial = {"foo": "initial value"}
    template_name = "form_template.html"

    def get(self, request, *args, **kwargs) :
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return render(request, self.template_name, {"form": form})