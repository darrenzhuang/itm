from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator
from .models import APInfo,SystemLogin

def index(request):
    return render(request, 'info/index.html')

def ap(request):
    aps_info = APInfo.objects.all()

    paginator = Paginator(aps_info, 18)  # Show 10 contacts per page.
    page_number = request.GET.get("page") # http://127.0.0.1:8000/?page=2
    page_obj = paginator.get_page(page_number)

    context = {
        'aps_info': page_obj
    }
    return render(request,'info/ap.html',context=context)


def office(request):
    return render(request, 'info/office.html')


def smart(request):
    return render(request, 'info/smart.html')

def system(request):
    system_list = SystemLogin.objects.all()

    paginator = Paginator(system_list, 18)  # Show 10 contacts per page.
    page_number = request.GET.get("page")  # http://127.0.0.1:8000/?page=2
    page_obj = paginator.get_page(page_number)

    context = {
        'system_list': page_obj
    }
    return render(request, 'info/system_login.html', context=context)

# def telinfo_detail(request, pk):
#     tel_info = TelephoneList.objects.get(id=pk)
#     return render(request, 'telinfo_detail.html', {'tel_info': tel_info})
#
#
# def telinfo_create(request):
#     if request.method == 'POST':
#         form = CreateTelephoneListForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("TelInfo Created")
#     else:
#             form = CreateTelephoneListForm()
#     return render(request, 'telinfo_create.html', {'form': form})