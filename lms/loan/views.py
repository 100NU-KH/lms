from django.views import generic
from django.db.models import Q
from .models import Application
from .forms import ApplicationForm, ApplicationSearchForm, ApplicationEditForm

class CreateApplication(generic.CreateView):
	form_class = ApplicationForm
	template_name = 'create.html'
	success_url = '/application/list/'

class ListApplications(generic.ListView, generic.edit.FormMixin):
	model = Application
	paginate_by = 10
	template_name = 'list.html'
	context_object_name = 'applications'
	form_class = ApplicationSearchForm

	def get_queryset(self):
		"""
		Return the list of items for this view.
		The return value must be an iterable and may be an instance of
		`QuerySet` in which case `QuerySet` specific behavior will be enabled.
		"""
		if self.queryset is not None:
			queryset = self.queryset
			if isinstance(queryset, QuerySet):
				queryset = queryset.all()
		elif self.model is not None:
			queryset = self.model._default_manager.all()
		else:
			raise ImproperlyConfigured(
				"%(cls)s is missing a QuerySet. Define "
				"%(cls)s.model, %(cls)s.queryset, or override "
				"%(cls)s.get_queryset()." % {
					'cls': self.__class__.__name__
				}
			)
		ordering = self.get_ordering()
		if ordering:
			if isinstance(ordering, str):
				ordering = (ordering,)
			queryset = queryset.order_by(*ordering)
		queryset = self.apply_search(queryset)
		return queryset

	def apply_search(self, queryset):
		"""
		Filter the queryset and set the description according to the search
		parameters given
		"""
		self.form = self.form_class(self.request.GET)
		if not self.form.is_valid():
			return queryset
		data = self.form.cleaned_data
		if data.get('country'):
			queryset = queryset.filter(Q(country=data.get('country')) | Q(country__icontains=data.get('country')) )
		
		if data.get('email'):
			queryset = queryset.filter(Q(email=data.get('email')) | Q(email__icontains=data.get('email')) )

		if data.get('status'):
			queryset = queryset.filter(Q(status=data.get('status')) | Q(status__icontains=data.get('status')) )
		return queryset

class UpdateApplication(generic.UpdateView):
	model = Application
	form_class = ApplicationEditForm
	template_name = 'update.html'
	success_url = '/application/list/'

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().post(request, *args, **kwargs)

class DeleteApplication(generic.DeleteView):
	model = Application
	success_url = '/application/list/'
	template_name = 'application_confirm_delete.html'