from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Text

class Post(Model):
  __tablename__ = "post"
  id = Column(Integer, primary_key=True)
  title = Column(String(250))
  content = Column(Text, default="")
