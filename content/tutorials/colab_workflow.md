---
title: Collaborative workflow
---

## A suggested collaborative workflow

If you have never collaborated in a coding project using version control before, here is a suggested workflow to get started.

This is based on trunk based development

### Project git structure

- `main` (previous default name was `master`) branch is the primary branch (i.e. the trunk)
- new versions are made using `git tag` on `main`
- all other branches on the remote are only for "backup/sync" reasons for individual developers
- follow the set branch name convention, e.g. `username/develop` or `username/the_work_to_do`

### Setup phase

If you are just joining into a project you probably need some setup to get going:

1. Enter the project. If you don't have it, then clone the repository first of course. If you do have it, get the latest changes with
    - `git checkout main`
    - `git pull`
1. Create a personal branch with `git checkout -b username/develop`

### Work flow

The workflow is always going to be: `main` is the single true source, your branches are ephemeral. But you should still experiment only locally and make sure everything works before you push `main` to the remote. There are two ways to do this:

#### Long-lived up-to-date branch

Every time you start coding

1. Open up project folder
1. Fetch remote version of `main`, this can be done with
    - `git checkout main`
    - `git pull` 
1. Switch to your personal branch `username/develop`, if you are not already there, with
    - `git checkout username/develop`
1. Make your branch up to date with `main` with
    - `git rebase main`
1. If there are conflicts, fix them (if you don't know how, see e.g. [Resolving merge conflicts after a Git rebase](https://docs.github.com/en/get-started/using-git/resolving-merge-conflicts-after-a-git-rebase)).

If you do not want to leave your personal branch to get the latest changes, you can do:

- `git fetch origin`
- `git rebase origin/main`

**Intense coding happens**

You are finishing up a task, you have made several commits with `git commit -m "meaningful message"` but are not done with _everything_, but done with a small unit that makes sense to push to everyone else. Now you need to again make sure you are up-to-date and that you did not break anything else. **Do not push changes that prevent others from doing their work**.

Go trough these steps to push the code:

1. Repeat the `fetch` + `rebase` above, fix any possible conflicts
1. Make sure the parts of the code that _should_ work, still works. This can be done with functional tests, unit tests or just by inspection.
1. Make sure that you have properly updated documentation and added your important changes to the changelog.
1. Fast forward `main` and push to the `remote`, this can be done with
    - `git checkout main`
    - `git merge username/develop`
    - `git push` (or `git push origin main`)

Now if you are working across multiple machines or want to back-up your work, you can do so by simply pushing your `username/develop` branch to the remote.

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
