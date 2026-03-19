#Imports from the blog.

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from organellebaseflask.auth import login_required
from organellebaseflask.db import get_db

#Grabbing my script now:


bp = Blueprint('search', __name__)

@bp.route('/')
@login_required
def organelle_search():
    return render_template('search/index.html')

