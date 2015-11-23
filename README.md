# Harbormaster

This is a simple web frontend for Docker. It does not have any support for swarms and multiple docker hosts but is focused
on a simple frontend for small setups.

## Things it does and should do

- [x] List all containers
- [x] Display pretty graph of all containers and ports
- [x] Start/Stop containers
- [x] View container details (docker inspect)
- [ ] Attach/log container
- [ ] Create containers
- [ ] Destroy containers
- [x] List all images
- [x] Display graph of images and parent images
- [ ] Pull images
- [ ] Manage mounted directories inside containers
- [ ] Recreate container with different settings
- [ ] Fetch (and cache for offline usage) the README of the docker images

## Screenshot
![Main interface](http://brixitcdn.net/github/harbormaster/main.png)