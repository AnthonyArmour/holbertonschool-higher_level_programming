#include "lists.h"
/**
 * is_palindrome - checks for palindrome
 * @head: linked list
 * Return: int
 */

int is_palindrome(listint_t **head)
{
	int ret = 1, x = 0, y = 0;
	int num[1024];
	listint_t *trav = NULL;

	if (!*head)
		return (1);
	trav = *head;
	while (trav->next)
	{
		num[x] = trav->n, x++;
		trav = trav->next;
	}
	num[x] = trav->n;
	for (y = 0; x > y; y++)
	{
		if (num[x] != num[y])
			ret = 0;
		x--;
	}
	return (ret);
}
