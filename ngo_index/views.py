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
        ngo = get_object_or_404(queryset, pk=pk)
        template_name = 'ngo_single.html'
        context = {
            'ngo': ngo
        }
        return render(request, template_name, context)


class NGO_Random(View):
    """
    View for displaying a random NGO page
    """
    def get(self, request, *args, **kwargs):
        queryset = NGO.objects.order_by('?')
        ngo = queryset.first()
        template_name = 'ngo_single.html'
        context = {
            "ngo": ngo
        }
        return render(request, template_name, context)


class SearchResults(generic.ListView):
    def querystring(self):
        """
        querystring method
        Required for retaining the same queryset across multiple -
        - pagination pages
        """
        querystring = self.request.GET.copy()
        querystring.pop(self.page_kwarg, None)
        encoded_querystring = querystring.urlencode()
        return encoded_querystring

    def get_queryset(self):
        """
        get_queryset method
        Constructs a queryset using Q methods
        Returns an object_list for use within the template
        """
        query = self.request.GET.get('search')
        object_list = NGO.objects.filter(
            Q(name__icontains=query) |
            Q(type__icontains=query) |
            Q(founders__icontains=query) |
            Q(director__icontains=query) |
            Q(region__icontains=query) |
            Q(location__icontains=query) |
            Q(headquarters__icontains=query) |
            Q(purpose__icontains=query)
            ).filter(approved=True)
        return object_list


class Contact(View):
    """
    View for contact page
    Could construct a queryset for users?
    """
    template_name = 'contact.html'


def http_404(request, exception):
    """
    Handles HTTP 404 Page Not Found errors
    """
    template_name = '404.html'
    return render(request, template_name)


def http_500(request):
    """
    Handles HTTP 500 Server Error errors
    """
    template_name = '500.html'
    return render(request, template_name)
