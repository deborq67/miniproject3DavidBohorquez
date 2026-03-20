#Imports from the blog.

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from organellebaseflask.auth import login_required
from organellebaseflask.db import get_db

#Grabbing my script now:

from organellebaseflask.organelle_ambiguity import initiate_search

bp = Blueprint('search', __name__)

@bp.route('/')
def organelle_search():
    return render_template('search/search.html')

@bp.route('/error')
def error_page():
   return render_template('search/error.html')

@bp.route('/search/<path:organism>')
@login_required
def search_organelle(organism):
    df, total_records = initiate_search(organism, g.user['username'])
    if df.empty:
        return redirect(url_for('search.error_page'))
    else:
        db = get_db()
        results = df.to_dict('records')

        result_id = db.execute(
            'INSERT INTO search (user_id, organism, result_count) VALUES (?, ?, ?)',
            (g.user['id'], organism, len(results)))
        search_id = result_id.lastrowid
        for result in results:
            db.execute(
                'INSERT INTO result (search_id, accession,title,bp_length,updated,ambiguity_percentage) VALUES (?, ?, ?, ?, ?, ?)',
                (search_id, result['Accession'], result["Title"], result["BP Length"], result['Updated'], result['Ambiguity Percentage']))
        db.commit()
        return render_template('search/results.html', results=results, organism=organism, total_records=total_records)

@bp.route('/history')
@login_required
def get_history():
    db = get_db()
    history = db.execute(
        'SELECT * FROM search WHERE user_id = ? ORDER BY created DESC',
        (g.user['id'],)
    ).fetchall()
    return render_template('search/history.html', history=history)
