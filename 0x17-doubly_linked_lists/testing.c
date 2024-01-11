#include <stdio.h>
#include <stdlib.h>

struct node
{
	int val;
	struct node *next;
	struct node *prev;
};
typedef struct node *node_t;

node_t add(node_t head, int valu)
{
	node_t tmp = malloc(sizeof(struct node));
	tmp->next = NULL;
	tmp->prev = NULL;
	tmp->val = valu;
	head = tmp;
	return head;
}

node_t addfirst(node_t head, int valu)
{
	node_t tmp = malloc(sizeof(struct node));
	tmp->next = head;
	tmp->prev = NULL;
	tmp->val = valu;
	head = tmp;
	return head;
}

node_t addlast(node_t head, int valu)
{
	node_t tp;
	node_t tmp = malloc(sizeof(struct node));
	tmp->prev = NULL;
	tmp->val=valu;
	tmp->next=NULL;
	tp = head;
	while (tp->next != NULL)
	{
		tp = tp->next;
	}
	tp->next=tmp;
	tmp->prev=tp;
	return head;
}
int main(void)
{
	node_t head = NULL;
	node_t ptr;
	head = add(head, 15);
	head = addfirst(head, 100);
	head = addfirst(head, 120);
	head = addfirst(head, 130);
	head = addlast(head, 190);

	ptr = head;
	while (ptr != NULL)
	{
		printf("%d -> ", ptr->val);
		ptr = ptr->next;
	}

	return (0);
}
