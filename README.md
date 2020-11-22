# Install
1. On the Docker host machine, install `nvidia-container-toolkit` and `nvidia-container-runtime` packages. See [the official install guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)
2. On the Docker host machine: type `nvidia-smi` and examine the CUDA version that appears on the right.

![nvidia-smi output](https://user-images.githubusercontent.com/20255278/95549635-4c40c600-0a10-11eb-9aa3-8ec628f3878e.png)

3. On the Docker host machine (replace the cuda version with the one you have installed), type:

```sh
docker run --rm --gpus all nvidia/cuda:10.1-base nvidia-smi
```

you should get the same output as you did when you ran the nvidia-smi on the host machine

4. In the file `/etc/docker/daemon.json` you should see:

```json
"runtimes": {"nvidia": { "path": "/usr/bin/nvidia-container-runtime","runtimeArgs": [] } }
```

If not, add it.

5. In your docker-compose YML, you should have:

```yaml
runtime: nvidia
```

6. Reboot to make sure the driver are all loaded. Alternatively you can try just running `sudo systemctl restart docker.service` but the result isn't garanteed.

[Source](https://github.com/docker/compose/issues/6691#issuecomment-705995189)

# How to run
Run this with

```sh
docker-compose up
```

or manually with

```sh
docker run --gpus all -it --rm sam1902/test-tensorflow:latest
```

# Troubleshooting

```sh
$ docker-compose up

Recreating test-tensorflow_test-tf_1 ... error

ERROR: for test-tensorflow_test-tf_1  Cannot create container for service test-tf: Unknown runtime specified nvidia

ERROR: for test-tf  Cannot create container for service test-tf: Unknown runtime specified nvidia
ERROR: Encountered errors while bringing up the project.
```

If you encouter this, make sure you followed step 4. in the [Install](#Install) section.
