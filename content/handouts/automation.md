---
title: "Automate away friction"
lecture: "11-automation"
weight: 11
---

## Automation tools

### snakemake

There are many good online tutorials on using different automation tools, to mention a few,
CodeRefinery has arranged [snakemake hackathons and tutorials](https://coderefinery.github.io/snakemake_hackathon/Snakemake_intro/). 

Research Software hour 005: Interview with Sarah Gibson, Snakemake, workflow automation intro, etc.
{{< youtube WIYaXzXLLY4 >}}

### Containers

[podman](https://podman.io/) is a great open source (and docker alternative) way of building,
managing, and running containers. There is a nice short [tutorial blog on
redhat](https://www.redhat.com/en/blog/write-your-first-containerfile-podman) detailing how to make
your own first container. If you want to play around with podman you can install it and have a look
at the `Containerfile`
[specification](https://manpages.ubuntu.com/manpages/jammy/man5/containers-dockerfile.5.html).

### Building

#### Generic

- [Meson Build](https://mesonbuild.com/)
- [GNU Make](https://www.gnu.org/software/make/)
- [waf](https://waf.io/)
- [SCons](https://scons.org/)
- [EasyBuild](https://docs.easybuild.io/)

#### Python

- [setuptools](https://setuptools.pypa.io/en/latest/)
- [hatch](https://hatch.pypa.io/latest/)
- [filt](https://flit.pypa.io/en/stable/)
- [pdm](https://pdm-project.org/en/latest/)

### Installing

- [python installer](https://installer.pypa.io/en/stable/)
- [arch packages](https://wiki.archlinux.org/title/Creating_packages)
- [ubuntu packages](https://canonical-ubuntu-packaging-guide.readthedocs-hosted.com/en/latest/)


### ansible

[Ansible](https://docs.ansible.com/) is a powerful open source automation tool that allows you to
execute tasks on a set of systems, be it local or remote. I have been using to manage the many
computers involved in the meteor camera network as well as for keeping my virtual machines up to
date.

### CI

- [GitLab CI](https://docs.gitlab.com/ci/)
- [Github Actions](https://github.com/features/actions)
- [Jenkins](https://www.jenkins.io/)
- [Ambient](https://ambient.liw.fi/)


## Environments and packages

- [Lmod](https://lmod.readthedocs.io/en/latest/)
- [pixi](https://pixi.sh/dev/)

## Why automation

A while back I read [this blog
post](https://dougseven.com/2014/04/17/knightmare-a-devops-cautionary-tale/) about a company that
owned about 400 million dollars in assets went bankrupt in about 45 minutes because of an error in a
manual deployment. It is an interesting story that I would recommend looking into. If you would
rather watch than read, there is of course a reaction video about the incident!

Bankrupt In 45 Minutes From DevOps | Prime Reacts
{{< youtube McRUxBHgFIo >}}


## Homework assignments

This task is simply to identify some workflow you have, whatever that may be, that would benefit
from automation, and then to automate it!
