from django import forms
from django.urls import reverse_lazy
from django.views import generic as views

from DjangoWebAdvanced.web.models import Todo


# Pure Python function
# - called with django request object
# - returns django response
def index(request):
    pass


class CreateTodoForm(forms.ModelForm):
    pass


# TemplateView
class IndexTemplateBaseView(views.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Class-based with TemplateView'
        return context

    # Optional:
    def dispatch(self, request, *args, **kwargs):
        # Custom logic for user access permissions
        return super().dispatch(request, *args, **kwargs)


# RedirectView - Provide a redirect on any GET request.
class RedirectToIndexView(views.RedirectView):
    url = reverse_lazy('cbv-index-template')

    # for custom logics use method 'get_redirect_url'
    def get_redirect_url(self, **kwargs):
        if ...:
            return "place 1"
        else:
            return "place 2"


# ListView
class TodosListView(views.ListView):
    model = Todo
    template_name = "todos-list.html"
    # context_object_name = "todos"
    ordering = ("-title", "category__name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'My TODO list'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('filter')
        if query:
            queryset = queryset.filter(title__contains=query)

        return queryset


# DetailsView
class TodoDetailsView(views.DetailView):
    model = Todo
    template_name = "todo-details.html"
    # context_object_name = "todo"

    def get_template_name(self):
        """
            # if admins -> show admin template
            # else -> show regular template
        """


# CreateView
class TodoCreateView(views.CreateView):
    model = Todo
    fields = "__all__"
    template_name = "todo-create.html"
    success_url = reverse_lazy("todos list")
    # form_class = CreateTodoForm

    # def get_form_class(self):
    #     pass

    # def get_success_url(self):
    #     pass
