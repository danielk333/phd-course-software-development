---
title: Public keys
---

## Public keys

This is a short overview of how to get your public key. This key is extremely useful for many
reasons, one of them being collaboration, remote access, and git hosting platforms. 

### Github/Gitlab

If you can push and pull to github or gitlab using ssh, you have already uploaded a key to their
website. You can find this key by going to `https://github.com/username.keys`. This is exactly the
same on gitlab, e.g. on our IRF instance it would be `https://gitlab.irf.se/username.keys`.

### Do i have a key?

To check if you have a key first run

```bash
ls ~/.ssh
```

If any of the results end in `.pub`, that is your public key. The name of the key is usually the
type of key it is (that is the default). For example mine is called `id_ed25519.pub` because it uses
the [Ed25519](https://en.wikipedia.org/wiki/EdDSA#Ed25519) schema.

> [!Varning]
> Do not share, upload, version control or otherwise send your PRIVATE key in any way. The private
> key is the one without the ".pub". Making this key public is like loosing your house key, and it
> sucks to change the locks.

### I do not have a key

Follow the [Use SSH keys to communicate with GitLab](https://docs.gitlab.com/user/ssh/) tutorial.

### Sharing your key

To share your public key when someone asks for it, you can either:

1. Send the `https://github.com/username.keys` link
1. Print the one with `cat ~/.ssh/id_KEY_TYPE.pub` and copy the text from the terminal
    - Or be fancy and use `cat ~/.ssh/id_KEY_TYPE.pub | xclip -selection clipboard` for X11
    - or `cat ~/.ssh/id_KEY_TYPE.pub | wl-copy` for Wayland, to get it directly into the clipboard

There are of course additional methods but these are the basic ones that should apply to most who
take this course.
