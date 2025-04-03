---
title: Collaborative workflow
---

## A suggested collaborative workflow

If you have never collaborated in a coding project using version control before, here is a suggested workflow to get started.

This is based on trunk based development

### Project git structure

- `main` branch is the primary branch (i.e. the trunk)
- "releases" are made using `git tag` on `main`
- all other branches on the remote are only for "backup/sync" reasons for individual developers
- use a personal branch name convention, e.g. `username/develop` or `username/the_work_to_do`

### Work flow

The workflow is always going to be `main` is the single true source, your branches are ephemeral. But you should still experiment only locally and make sure everything works before you push `main` to the remote. There are two ways to do this:

#### Long-lived up-to-date branch

Every time you start coding

1. Open up project folder
1. Fetch remote version of `main`, this can be done with
  - `git fetch origin main:main` or
  - `git checkout main` and then `git pull` (or `git pull origin main`) 
1. Switch to your personal branch `username/develop`, if you are not already there, with
  - `git checkout username/develop`
1. Make your branch up to date with `main` with
  - `git rebase main`

If there are conflicts, fix them (if you don't know how, see e.g. [Resolving merge conflicts after a Git rebase](https://docs.github.com/en/get-started/using-git/resolving-merge-conflicts-after-a-git-rebase)).

**Intense coding happens**

You are finishing up for the day, you have made several commits with `git commit -m ""` but are not done with the work. Now you need to again make sure you are up-to-date and that you did not break anything else. So go trough these steps:

1. Repeat the `fetch` + `rebase` above, fix any possible conflicts
1. Make sure the parts of the code that _should_ work, still works. This can be done with functional tests, unit tests or just by inspection
1. Fast forward `main` and push to the `remote`, this can be done with
  - `git checkout main` and `git merge username/develop`, then `git push` (or `git push origin main`)

Now if you are working across multiple machines or want to back-up your work without fast-forwarding master, you can do so by simply pushing your `username/develop` branch to the remote and saving the `main` fast-forward for later.

### Ephemeral branches

1. Open up project folder, there are no other branches, only `main`
1. `git pull` to get latest changes
1. `git checkout -b username/feature` make a new branch
1. **Intense coding happens**
1. `git checkout main` and `git pull`
1. `git merge username/feature` and `git push`

### No branches

1. Open up project folder, there are no other branches, only `main`
1. `git pull`
1. **Intense coding happens** `git commit -m "Good commit message"`
1. `git pull --rebase`
1. `git push`
