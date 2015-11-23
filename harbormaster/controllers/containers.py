from harbormaster import app
from harbormaster.components import docker
from flask import redirect, url_for, request, render_template, render_template_string, jsonify


@app.route('/')
def instances():
    d = docker.get_docker()
    context = {
        "containers": [],
        "ports": [],
        "links": [],
        "primary_name": {}
    }
    container_id = {}
    for container in d.containers(all=True):
        print(container)
        container['up'] = 'Up' in container['Status']
        context['containers'].append(container)
        primary_name = ""
        for name in container['Names']:
            container_id[name[1:]] = container['Id']
            if '/' not in name[1:]:
                primary_name = name[1:]

        for name in container['Names']:
            context['primary_name'][name] = primary_name

        for port in container['Ports']:
            public = ''
            if 'PublicPort' in port:
                public = "{IP}:{PublicPort}".format(**port)
            context['ports'].append({
                'container': container,
                'private': port['PrivatePort'],
                'type': port['Type'],
                'public': public
            })

    for container in d.containers(all=True):
        inspect = d.inspect_container(container['Id'])
        links = inspect['HostConfig']['Links']
        if links:
            for link in links:
                a, b = link.split(':')
                a = container_id[a[1:]]
                b, label = b[1:].split('/')

                context['links'].append({
                    'a': a,
                    'b': container_id[b],
                    'label': label
                })

        print(inspect)
    return render_template('containers.html', **context)


@app.route('/container/<container>/action/<action>')
def container_action(container, action):
    d = docker.get_docker()
    if action == 'start':
        d.start(container)
    elif action == 'stop':
        d.stop(container)
    return redirect(url_for('instances'), code=303)
