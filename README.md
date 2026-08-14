# simple-fastapi-ng

Simple [FastAPI] container application.

> [!IMPORTANT]
> This container version contains `instana` package installed but not activated.
>
> To know more about activating Instana without code changes, read the [documentation here].


## Prerequisites

- [uv]
- [Podman]

## Building

```shell
podman build \
    --platform linux/amd64,linux/arm64 \
    -f ContainerFile \
    --manifest simple-fastapi:instana-autowrapt . 
```

## Running

```shell
podman run \
    -p 8000:8000 \
    -e AUTOWRAPT_BOOTSTRAP=instana \
    simple-fastapi:instana-autowrapt
```

### Local Development mode

```shell
AUTOWRAPT_BOOTSTRAP=instana uv run fastapi dev main.py
```

### Local Production mode

```shell
AUTOWRAPT_BOOTSTRAP=instana uv run fastapi run main.py --port 8000 --host 0.0.0.0
```


[FastAPI]: https://fastapi.tiangolo.com "FastAPI"
[OpenShift]: https://www.redhat.com/en/technologies/cloud-computing/openshift "RedHat OpenShift"
[uv]: https://docs.astral.sh/uv/ "uv"
[Podman]: https://podman.io/ "Podman"
[documentation here]: https://ibm.biz/monitor-python#activating-without-code-changes "Monitoring Python"
