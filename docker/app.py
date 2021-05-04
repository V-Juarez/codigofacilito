impor docker

client = docker.DockerClient("unix://var/run/docker.sock")

for container in client.containers.list():
	print(contianer.name)

for container in client.images.list():
	print(container.id)
