#include "lists.h"
/**
 * insert_node - inserts node in numerical order
 * @head: head of list
 * @number: value of new node
 * Return: address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *trav = NULL;
	int sig = 0;

	temp = malloc(sizeof(listint_t));
	if (!temp)
		return (NULL);
	temp->n = number;
	temp->next = NULL;
	trav = *head;
	if (!*head)
	{
		*head = temp;
		return (temp);
	}
	while (trav->next)
	{
		if (temp->n > trav->n && temp->n <= trav->next->n)
		{
			temp->next = trav->next;
			trav->next = temp;
			sig = 1;
		}
		trav = trav->next;
	}
	if (sig == 0)
	{
		trav->next = temp;
	}
	return (temp);
}
