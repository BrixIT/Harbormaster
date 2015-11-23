from harbormaster import app
from harbormaster.components import docker
from flask import redirect, url_for, request, render_template, render_template_string, jsonify


@app.route('/images')
def images():
    d = docker.get_docker()
    images = d.images(all=True)
    return render_template('images.html', images=images)