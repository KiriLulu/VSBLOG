from flask_admin import BaseView,expose
from flask_admin.contrib.sqla  import ModelView
from ..forms import CKTextAreaField

class CustomView(BaseView):
	@expose('/')
	def index(self):
		return self.render('admin/custom.html')
		
class CustomModelView(ModelView):
	pass
	
class PostView(ModelView):
	form_overrides = dict(text = CKTextAreaField)
	column_searchable_list = ('text','title')
	column_filters = ('published_date',)
	create_template = 'admin/post_edit.html'
	edit_template = 'admin/post_edit.html'