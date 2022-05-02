#include<stdio.h>

typedef struct node* tree_pointer;

int node_cnt = 9;
int cnt = 0;


typedef struct node {
	char data[5];
	tree_pointer leftChild, rightChild;
}Node;

int isend() {
	cnt++;
	if (cnt == node_cnt) {
		cnt = 0;
		return;
	}
	printf("-> ");
}

void inorder(tree_pointer ptr) {
	if (ptr->leftChild == NULL) {
		printf("%s ",ptr->data);
		isend();
		return;
	}
	inorder(ptr->leftChild);
	printf("%s ", ptr->data);
	isend();
	inorder(ptr->rightChild);
}

void preorder(tree_pointer ptr) {
	if (ptr->leftChild == NULL) {
		printf("%s ", ptr->data);
		isend();
		return;
	}
	printf("%s ", ptr->data);
	isend();
	preorder(ptr->leftChild);
	preorder(ptr->rightChild);
}

void postorder(tree_pointer ptr) {
	if (ptr->leftChild == NULL) {
		printf("%s ", ptr->data);
		isend();
		return;
	}
	postorder(ptr->leftChild);
	postorder(ptr->rightChild);
	printf("%s ", ptr->data);
	isend();
}

void main() {
	Node J = {"J",NULL,NULL};
	Node I = {"I",NULL,NULL};
	Node D = {"D",&J,&I};
	Node E = {"E",NULL,NULL};
	Node F = {"F",NULL,NULL};
	Node G = {"G",NULL,NULL};
	Node B = {"B",&D,&E};
	Node C = {"C",&F,&G};
	Node A = {"A",&B,&C};

	printf("INORDER 방식:");
	inorder(&A);
	printf("\n");

	printf("PREORDER 방식:");
	preorder(&A);
	printf("\n");

	printf("POSTORDER 방식:");
	postorder(&A);
	printf("\n");

}