#include <python.h>
#include <stdio.h>


/**
* print_python_list_info - prints some basic info about Python lists.
* @p: pointer to a list
* Return: void
*/

void print_python_list_info(PyObject *p)
{
	int i, len;
	PyObject *elm;

	len = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < len; i++)
	{
		elm = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(elm)->tp_name);
	}
}
