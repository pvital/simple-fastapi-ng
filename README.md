# simple-fastapi-ng

Simple [FastAPI] container application running with [Gunicorn].

## Prerequisites

- [uv]
- [Podman]

## Building

```shell
podman build \
    -f ContainerFile \
    -t simple-fastapi:gunicorn . 
```

## Running

```shell
podman run -p 8000:8000 simple-fastapi:gunicorn
```

### Local Development mode

```shell
uv run fastapi dev main.py
```

### Local Production mode

```shell
uv run gunicorn main:app --worker-class asgi --bind 0.0.0.0:8000 --workers 4
```


[FastAPI]: https://fastapi.tiangolo.com "FastAPI"
[OpenShift]: https://www.redhat.com/en/technologies/cloud-computing/openshift "RedHat OpenShift"
[uv]: https://docs.astral.sh/uv/ "uv"
[Podman]: https://podman.io/ "Podman"
[Gunicorn]: https://gunicorn.org/ "Gunicorn"
