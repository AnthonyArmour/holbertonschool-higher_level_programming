#include "lists.h"
/**
 * check_cycle - checks linked list for loop
 * @list: linked list
 * Return: 1 for cycle and 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
