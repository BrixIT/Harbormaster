from harbormaster import app
from harbormaster.components import docker
from flask import redirect, url_for, request, render_template, render_template_string, jsonify


@app.route('/container/<container_id>/details')
def container_details(container_id):
    d = docker.get_docker()
    context = {}
    context['inspect'] = d.inspect_container(container_id)
    print(context)
    return render_template('containerdetails.html', **context)
