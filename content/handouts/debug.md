---
title: "Making it work: debugging"
lecture: "09-debug"
weight: 9
---


## Asserts

Asserts is an interesting concept in programming as it allows you to assert things about your data
that should be true at runtime. Asserts can help you find errors in those assumptions or find bugs
that produce data that does not follow those assumptions as they will crash the program if the
assertion fails.

This is obviously something that you sometimes do not want for e.g. performance or
robustness concerns. For example, if you want tests to fail quickly using asserts to find problems
but then when you deploy your software, say to run an entire instrument network, you dont want a
small erroneous data packet to crash the entire network, but you still want to be able to find this
error somewhere in the logs of your system. In this case, error handling via exceptions are the
easier choice. Assertions can be turned off at runtime while exceptions can not.

As such, I think a mix between using asserts and proper error handling, depending on your
application, is the way to go.

Below is a video that talks about using asserts instead of comments that describe the assumptions
which is an interesting way to think about their usage.

Low Level Game Dev - Don't write comments, do this instead!
{{< youtube gHRRTCKtUSc >}}


## Static analysis

One of the static analysis tools that orient towards finding security issues is [grype](https://github.com/anchore/grype), below is a short podcast that discusses this tool.

Open Source Security - Syft, Grype, and Grant with Alan Pope
{{< youtube Lgt_MrRCQ5M >}}

## Program to debug

In order to have a sufficiently problematic program to debug I have crafted [this example](code/python-scripts/hard_to_fix.py). To run the code, first run the script in one terminal with the argument `server` and then in another with the argument `client`.

In this example, the error message will not be helpful at all. You will need to somehow inspect the
data that is being exchanged to find the error.

One tip is to know what post mortem in [pdb](https://docs.python.org/3/library/pdb.html) is.

The code:

{{< include-code "python" "code/python-scripts/hard_to_fix.py" "">}}
