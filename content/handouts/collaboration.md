---
title: "Collaboration"
lecture: "06-collaboration"
weight: 6
---

## Workflow

{{< tutorial colab_workflow "For a suggested first time workflow, see" >}}

There are also a few websites that go trough a lot of material on git workflows:

- [Patterns for Managing Source Code Branches](https://martinfowler.com/articles/branching-patterns.html#BasePatterns)
- [Trunk-Based Development](https://trunkbaseddevelopment.com/)

## Python project templates

{{< tutorial python_project "For python project templates, see" >}}

## Public keys

{{< tutorial public_keys "For instructions on how to get your public key, see" >}}

## Git material

### Pro Git book

There is a open source book published under a Creative Commons licence called Pro Git V2 which is
really good and I can highly recommended. You can find it compiled on [git-scm
book](https://git-scm.com/book/en/v2) with the source here on
[github.com/progit/progit2](https://github.com/progit/progit2). I have used some of the figures from
this book in the lecture as they very well explain the ins-and-outs of git! They are included in
this repository and of course licensed under the same licence as the book is licensed under
([Attribution-NonCommercial-ShareAlike 3.0
Unported](https://creativecommons.org/licenses/by-nc-sa/3.0)).

### Oh-my-git

A interactive game to learn git! Highly recommended!

- [Oh-my-git](https://ohmygit.org/)

### CodeRefinery

I can really recommend everyone go trough the CodeRefinery [Introduction to version control with Git - Why we want to track versions and how to go back in time to a working version](https://coderefinery.github.io/git-intro/). 

This written material above is walked trough in workshop in the following two videos

1.2 Git Intro (day 1) - CodeRefinery 2025 Mar
{{< youtube 0u2K7KJBL-U >}}

2.2 Git Intro day 2 - CodeRefinery 2025 Mar
{{< youtube 8uay_XoNRck >}}

There is also follow-up material called [git collaborative](https://coderefinery.github.io/git-collaborative/) that was also arranged into a recorded workshop here:

3.2 Git collaborative - CodeRefinery 2025 Mar
{{< youtube 4Uf7eVSCZeU >}}

### Other resources

A few other good resources are:

- [Good set of standard `.gitignore` files](https://github.com/github/gitignore)
- **More to be added here**

### Get git status in command line

There are several ways you can get the git status in to the commend line prompt, one of the easiest is by using something like [starship](https://starship.rs/). 

To manually make this happen, you can follow the [A1.6 Appendix A: Git in Other Environments - Git in Bash](https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-Bash) guide.

### Git tools

The one tool that I would recommend for working with git is []()

There are other tools out there such as [Meld](https://gnome.pages.gitlab.gnome.org/meld/#)and also
really good tools for editors such as VSCode. For NeoVim I use [fugutive.vim](https://github.com/tpope/vim-fugitive), it helps me work with git directly in my editor. Below is a video that showcases this is practice:

DevOps Toolbox - Resolve Git Merge Conflicts with Neovim and Fugitive!
{{< youtube vpwJ7fqD1CE >}}

## License

Having a license is also vital to collaboration. To learn more I very much recommend the [choosealicense.com](https://choosealicense.com/) website.

It is important to consider that code and data often have different licenses and needs to be treated
differently. In the end intellectual property, licenses and copy-rights are legal matters which is
outside the scope of this course and also vary from contract to contract, university to institute
and country to country.

Some material such as images and other creative material fit much better under a Creative Commons
license, you can read more about these at [About CC Licenses](https://creativecommons.org/share-your-work/cclicenses/).

Still it is good to know that the standard in Sweden for researchers at universities is to have
something called the "teachers exemption", you can read more about it on this [wiki page](https://sv.wikipedia.org/wiki/L%C3%A4rarundantag) or on the [Union webpages (Upphovsrätt till forskningsdata och forskningsmaterial)](https://sulf.se/jobb-lon-och-villkor/upphovsratt/upphovsratt-till-forskningsdata-och-forskningsmaterial/).


The following video is also a nice summary of the most common licenses:

The Linux Experiment - Free and Open Source software licenses explained
{{< youtube UMIG4KnM8xw >}}


## Talks about trunk based development

code.talks 2023 - Our journey from Gitflow to Trunk Based Development
{{< youtube DDkjBqlks40 >}}

Also the start of this talk is a nice overview of why long lived branches can be problematic: [Real Programmers Commit To Master - Jakob Ehn](https://www.youtube.com/watch?v=hL1OZfgoZGk).


## Creating your own "remote"

First you are going to need what is called a "bare" repository at the remote site that you have ssh
access to:

```bash
git init --bare name_of_my_repo.git
```

This command will create an empty repository in a folder `name_of_my_repo.git` that is specialized for being a remote repository.

You can then add this repository as a remote on you local machine in the project `name_of_my_repo` with:

```bash
git remote add my_server ssh://username@hostname:port/path/to/name_of_my_repo.git
```

And that is it! As long as you can ssh to the server `username@hostname:port`, you can git push and
pull like any other git hosting platform! You can even do this locally towards a USB stick or just
on your own harddrive for moving later with

```bash
git remote add my_remote /path/to/name_of_my_repo.git 
```

For a full guide, have a look at [Getting Git on a Server](https://git-scm.com/book/en/v2/Git-on-the-Server-Getting-Git-on-a-Server).


## Notes from lecture

In the live lecture we ended up going trough the "Python project template" and one of the things
that came up was the [GitLab CI/CD YAML syntax](https://docs.gitlab.com/ci/yaml/). We will deep dive
into this later in the lecture on *Automation* but some things came up during the lecture that I was
not sure about so here are those explained/corrected:

[`expire_in`](https://docs.gitlab.com/ci/yaml/#artifactsexpire_in)
: `expire_in` specify how long job artifacts are stored before they are deleted. This setting **does not** affect artifacts from the latest job, *unless* this is disabled in the settings at the project level or instance-wide.

[`pages`](https://docs.gitlab.com/ci/yaml/#pages)
: In the current version in the repository I used the job-name `pages` together with the artifact
`public` to indicate that GitLab pages should be built and published. However, it turns out that
using the job-name is now a deprecated method (!) and one should instead use `pages: true`.


## Fun detour

On the topic of collaboration, for a funny break from studying you can watch someone run random
peoples code on his programmable Christmas tree!

I run untested, viewer-submitted code on my 500-LED christmas tree.
{{< youtube v7eHTNm1YtU >}}


## Homework

### Recommended listening

The podcast "CodingBlocks" did a small series called "Git from the bottom up" a few years ago. This podcast really opened my eyes about how git works. Even though it might go into detail I don't use every day I really think some of the understanding has really improved my git workflow.

As a warm-up or if you are very new to git, you can first listen to the [Understanding Git](https://www.codingblocks.net/podcast/understanding-git/) episode.

Listening trough these will take some time so take this as a long term goal. The episodes are linked in order below:

- [Blobs and Trees](https://www.codingblocks.net/episode191)
- [Commits](https://www.codingblocks.net/episode192)
- [Rebasing](https://www.codingblocks.net/episode193)
- [The Index](https://www.codingblocks.net/episode194)
- [Reset, Stash, and Reflog](https://www.codingblocks.net/episode195)

Then as a follow up, they also had an episode that covered different workflows that might be very relevant called [Comparing Git workflows](https://www.codingblocks.net/podcast/comparing-git-workflows/).
