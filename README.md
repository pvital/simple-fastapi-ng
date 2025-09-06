# simple-fastapi-ng

Simple [FastAPI] container application.

## Prerequisites

- [uv]

## Building

```shell
podman build --platform linux/amd64,linux/arm64 -f ContainerFile -t simple-fastapi:latest . 
```

## Running

```shell
podman run -p 8000:8000 simple-fastapi:latest
```

### Local Development mode

```shell
uv run fastapi dev main.py
```

### Local Production mode

```shell
uv run fastapi run main.py --port 8000 --host 0.0.0.0
```


[FastAPI]: https://fastapi.tiangolo.com "FastAPI"
[OpenShift]: https://www.redhat.com/en/technologies/cloud-computing/openshift "RedHat OpenShift"
[uv]: https://docs.astral.sh/uv/ "uv"
