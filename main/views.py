from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, TemplateView
from .forms import ServiceCreateForm, RegistrationUserForm, LoginUserForm
from django.shortcuts import render, get_object_or_404
from .models import Services, ServicesDetail, Order


class IndexView(TemplateView):
    model = Services
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services_list'] = Services.objects.all().order_by('-id')[:5]
        return context


class ProfileView(TemplateView):
    template_name = 'templates/profile.html'


class ServiceView(generic.ListView):
    model = Services
    template_name = 'templates/service.html'

    def get_queryset(self):
        return Services.objects.all()


class ServiceDetailView(generic.DetailView):
    model = ServicesDetail
    template_name = 'templates/service_detail.html'

    def get_queryset(self):
        return ServicesDetail.objects.all()


class LoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('index')


class LogoutView(LogoutView):
    template_name = 'index.html'


class RegistrationView(CreateView):
    form_class = RegistrationUserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


def service_detail(request, pk):
    services = get_object_or_404(Services, pk=pk)

    return render(request, "templates/service_detail.html", {'service': services})


def order_service(request, service_id):
    service = get_object_or_404(Services, pk=service_id)

    if request.method == 'POST':
        order = Order.objects.create(user=request.user, service=service)

        return redirect('profile')

    return render(request, 'profile.html', {'service': service})

@login_required
def create_service(request):
    if request.method == 'POST':
        form = ServiceCreateForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.save()
            return redirect('service_list')
    else:
        form = ServiceCreateForm()
    return render(request, 'templates/create_service.html', {'form': form})


def search_view(request):
    query = request.GET.get('query', '')
    results = []

    if query:
        results = Services.objects.filter(title__icontains=query)

    context = {'results': results}
    return render(request, "templates/search_results.html", context)