from docker import Client


def get_docker():
    return Client(base_url='unix://docker.sock')
