#include "lists.h"
/**
 * check_cycle - check if a linked list has a cycle.
 *
 * @list: linked list
 *
 * Return: Always 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast)
	{
		slow = slow->next;
		if (fast->next == NULL)
			break;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
		if (fast == NULL)
			return (0);
	}
	return (0);
}
