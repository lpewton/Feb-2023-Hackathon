from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from .models import NGO


class LandingPage(generic.ListView):
    """
    landing page view
    """
    model = NGO
    template_name = 'index.html'
    paginate_by = 3
    queryset = NGO.objects.order_by('-founded')


class NGO_Directory(generic.ListView):
    """
    view for displaying all NGOs
    """
    model = NGO
    template_name = 'ngo_directory.html'
    paginate_by = 6
    queryset = NGO.objects.order_by('-founded')


class NGO_Single(View):
    """
    View for displaying information about a single NGO
    """
    def get(self, request, pk, *args, **kwargs):
        """
        Get method for retrieving a particular record
        """
        queryset = NGO.objects
        ngo = get_object_or_404(queryste, pk=pk)
        template_name = 'ngo_single.html'
        context = {
            'NGO': ngo
        }
        return render(request, template_name, context)
