from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CryptoAlertForm
from .models import CryptoAlert
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .tasks import check_crypto_prices
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

@login_required
def create_alert(request):
    if request.method == 'POST':
        form = CryptoAlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user
            alert.save()
            messages.success(request, "Alerte créée avec succès!")
            return redirect('list_alerts')
    else:
        form = CryptoAlertForm()
    return render(request, 'alerts/create_alert.html', {'form': form})

@login_required
def list_alerts(request):
    alert_list = CryptoAlert.objects.filter(user=request.user)
    paginator = Paginator(alert_list, 5)  # 5 alertes par page

    page = request.GET.get('page')
    try:
        alerts = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, affichez la première page.
        alerts = paginator.page(1)
    except EmptyPage:
        # Si la page est hors de portée (par exemple, 9999), affichez la dernière page.
        alerts = paginator.page(paginator.num_pages)

    return render(request, 'alerts/list_alerts.html', {'alerts': alerts})

@login_required
def show_alert(request, alert_id):
    alert = get_object_or_404(CryptoAlert, id=alert_id)
    return render(request, 'alerts/show_alert.html', {'alert': alert})

@login_required
def update_alert(request, alert_id):
    alert = get_object_or_404(CryptoAlert, id=alert_id)
    if request.method == 'POST':
        form = CryptoAlertForm(request.POST, instance=alert)
        if form.is_valid():
            form.save()
            return redirect('list_alerts')
    else:
        form = CryptoAlertForm(instance=alert)
    return render(request, 'alerts/update_alert.html', {'form': form})

@login_required
def delete_alert(request, alert_id):
    alert = get_object_or_404(CryptoAlert, id=alert_id)
    if request.method == 'POST':
        alert.delete()
        return redirect('list_alerts')
    return render(request, 'alerts/delete_alert.html', {'alert': alert})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_alerts')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
