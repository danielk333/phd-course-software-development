#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <string.h>

static PyObject* say_hello(PyObject *self, PyObject *args)
{
    const char *name;
    if (!PyArg_ParseTuple(args, "s", &name)) 
    {
        return NULL;
    }
    
    size_t n = strlen(name);
    size_t response_len = 7 + n + 1;
    char *response = (char *)malloc(response_len);
    if (!response) {
        return PyErr_NoMemory();
    }

    strcpy(response, "Hello, ");
    strcat(response, name);

    PyObject *ret = Py_BuildValue("s", response);
    free(response);
    return ret;
}

/* Table of what is in this modeule*/
static PyMethodDef BarMethods[] = 
{
    {"hello", say_hello, METH_VARARGS,
     "Greets you!"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

/* Definition of the module */
static struct PyModuleDef barmodule = {
    PyModuleDef_HEAD_INIT,
    "bar",    /* name of module */
    NULL,     /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    BarMethods
};

/* This actually creates the module using the module definition */
PyMODINIT_FUNC PyInit_bar(void)
{
    return PyModule_Create(&barmodule);
}
