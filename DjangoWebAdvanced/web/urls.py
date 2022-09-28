from django.urls import path

from DjangoWebAdvanced.web.views import IndexTemplateBaseView, RedirectToIndexView, \
        TodosListView, TodoDetailsView, TodoCreateView


urlpatterns = [
        path('cbv-template/', IndexTemplateBaseView.as_view(), name='cbv-index-template'),
        path('cbv-redirect/', RedirectToIndexView.as_view(), name='cbv-redirect'),
        path('todos-list/', TodosListView.as_view(), name='todos list'),
        path('todo/<int:pk>', TodoDetailsView.as_view(), name='todos details'),
        path('todo-create/', TodoCreateView.as_view(), name='todos create'),
]
