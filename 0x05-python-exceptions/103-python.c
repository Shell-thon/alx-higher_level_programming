#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/*
 * print_python_list - Print basic info about Python lists
 * @p: Pointer to a Python object
 */
void print_python_list(PyObject *p)
{
PyListObject *list;
Py_ssize_t size, i;
PyObject *item;

if (p == NULL || !PyList_Check(p))
{
printf("[ERROR] Invalid List Object\n");
return;
}

list = (PyListObject *)p;
size = PyList_Size(list);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(list, i);
printf("Element %ld: %s\n", i, item->ob_type->tp_name);
}
}

/*
 * print_python_bytes - Print basic info about Python bytes
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
PyBytesObject *bytes;
Py_ssize_t size, i;
char *data;

if (p == NULL || !PyBytes_Check(p))
{
printf("[ERROR] Invalid Bytes Object\n");
return;
}

bytes = (PyBytesObject *)p;
size = PyBytes_Size(bytes);
data = PyBytes_AsString(bytes);

printf("[*] Python bytes info\n");
printf("[*] Size of the Python Bytes = %ld\n", size);
printf("[*] Trying string: %s\n", data);
printf("[*] First %ld bytes: ", size < 10 ? size : 10);

for (i = 0; i < size && i < 10; i++)
printf("%02x ", data[i] & 0xff);
printf("%s\n", size < 10 ? "" : "...");
}

/*
 * print_python_float - Print basic info about Python floats
 * @p: Pointer to a Python object
 */
void print_python_float(PyObject *p)
{
PyFloatObject *float;
double val;

if (p == NULL || !PyFloat_Check(p))
{
printf("[ERROR] Invalid Float Object\n");
return;
}

float = (PyFloatObject *)p;
val = PyFloat_AsDouble(float);

printf("[*] Python float info\n");
printf("[*] Float value: %f\n", val);
}
