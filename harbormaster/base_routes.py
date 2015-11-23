import os
from flask import session, redirect, url_for, request, flash, render_template, jsonify, send_from_directory
from harbormaster import app


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
