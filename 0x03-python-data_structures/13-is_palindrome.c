#include "lists.h"
#include <stddef.h>

/**
 * reverse_list - reverses a linked list
 * @head: head node of linked list
 * 
 * Return: reversed list
*/

listint_t *reverse_list(listint_t *head) 
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/**
 * is_palindrome - checks if a singly linked list is a plaindrome
 * @head: head node of singly linked list
 * 
 * Returns: 0 if not palindrome and 1 if is palindrome
*/

int is_palindrome(listint_t **head)
{
    listint_t *slow_ptr = *head;
    listint_t *fast_ptr = *head;
    listint_t *second_half;
    listint_t *prev_slow_ptr = *head;
    int is_palindrome = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast_ptr != NULL && fast_ptr->next != NULL)
        {
            fast_ptr = fast_ptr->next->next;
            prev_slow_ptr = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        if (fast_ptr != NULL)
        {
            slow_ptr = slow_ptr->next;
        }

        second_half = reverse_list(slow_ptr);

        while (*head != NULL && second_half != NULL)
        {
            if ((*head)->n != second_half->n)
            {
                is_palindrome = 0;
                break;
            }
            *head = (*head)->next;
            second_half = second_half->next;
        }

        second_half = reverse_list(second_half);
        prev_slow_ptr->next = second_half;
    }

    return (is_palindrome);
}
