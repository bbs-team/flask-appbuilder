from flask import render_template
from flask_babel import gettext as __, lazy_gettext as _
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db
from app.models import Post

class PostModelView(ModelView):
  datamodel = SQLAInterface(Post)

  list_title = _('List post')
  add_title = _('Add post')
  edit_title = _('Edit post')
  show_title = _('Show post')

  label_columns = {
    "title": _("post title"),
    "content": _("post content")
  }

appbuilder.add_view(
  PostModelView,
  "Post",
  icon="fa-file-text",
  label=_('Post Menu')
)

"""
    Application wide 404 error handler
"""
    
@appbuilder.app.errorhandler(404)
def page_not_found(e):
  return (
    render_template(
      "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
    ),
    404,
  )

db.create_all()
