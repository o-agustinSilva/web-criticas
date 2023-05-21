from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Inicio(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
      context = super().get_context_data(**kwargs)
      return context
