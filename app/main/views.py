from flask import render_template,request,redirect,url_for,abort
from . import main
# from ..request import get_movies,get_movie,search_movie
# from .forms import ReviewForm,UpdateProfile
# from .. import db,photos
from ..models import ReviewUser
from flask_login import login_required,current_user
# import markdown2 
,