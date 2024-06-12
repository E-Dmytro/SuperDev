from django.shortcuts import render, redirect
from django.views.generic import ListView
from order.models import Employee
from .forms import EmployeeForm
from .models import Employee

# class AuthorList(ListView):
#
#     model = employee
#     template_name = "employee/index.html"
#     context_object_name = "authors"
#
#
#
#     def get_context_data(self, **kwargs):
#
#         context = super(AuthorList, self).get_context_data(**kwargs)
#         context['title'] = 'Список авторів'
#         context['content_title'] = 'Адміністрування бібліотеки / Автори книг'
#
#         return context
#
#     def get_queryset(self):
#
#         queryset = employee.get_all()
#
#         return queryset



# ##### new


def author_list(request):
    context = {'author_list':employee.objects.all()}
    return render(request,'employee/author_list.html', context)

def author_create(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AuthorForm()
        else:
            employee = employee.objects.get(pk=id)
            form = AuthorForm(instance=employee)
        return render(request, 'employee/author_create.html', {'form':form})
    else:
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            employee = employee.objects.get(pk=id)
            form=AuthorForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def author_delete(request,id):
    employee = employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')