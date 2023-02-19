from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from .models import NGO, Message
from .forms import MessageForm


class LandingPage(generic.ListView):
    """
    landing page view
    """
    model = NGO
    template_name = 'index.html'
    paginate_by = 3
    queryset = NGO.objects.order_by('founded')


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
    """
    View for rendering the search results page
    """
    model = NGO
    template_name = 'search_results.html'
    paginate_by = 4

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
            )
        return object_list


class Contact(generic.CreateView):
    """
    View for contact page
    CreateView is used to handle the message form submission
    """
    model = Message
    form_class = MessageForm
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        """
        Post method to handle form submission
        """
        template_name = 'contact.html'

        message_form = MessageForm(request.POST)

        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.save()

            context = {
                "message_form": MessageForm(),
                "submitted": True
            }

            return render(request, Contact.template_name, context)

        else:
            message_form = MessageForm()

            context = {
                "message_form": MessageForm(),
                "submitted": False,
                "failure": True
            }

            return render(request, Contact.template_name, context)


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
