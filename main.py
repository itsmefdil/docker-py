import docker
from typing import Union

from fastapi import FastAPI

app = FastAPI()
docker_client = docker.from_env()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/containers")
def container():
    try:
        containers = docker_client.containers.list()
        container_list = [
            {
                "id": container.id,
                "name": container.name,
                "status": container.status,
                "image": (
                    container.image.tags[0] if container.image.tags else "untagged"
                ),
            }
            for container in containers
        ]
        return {"containers": container_list}
    except Exception as e:
        return {"error": str(e)}


@app.get("/containers/{container_name}")
def container(container_name: str):
    try:
        container = docker_client.containers.get(container_name)
        container_info = {
            "id": container.id,
            "name": container.name,
            "status": container.status,
            "image": container.image.tags[0] if container.image.tags else "untagged",
        }
        return {"container": container_info}
    except Exception as e:
        return {"error": str(e)}