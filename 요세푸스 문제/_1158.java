package _1158;

import java.util.ArrayList;
import java.util.Scanner;

public class _1158 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		CircularLinkedList arr = new CircularLinkedList();
		int N,K;
		N = input.nextInt();
		K = input.nextInt();
		for (int i = 0; i < N; i++)				//���� ���Ḯ��Ʈ�� �ʱ�ȭ
			arr.add(i + 1);
		System.out.print("<");
		Node p = arr.tail;
		while(true) {
			for (int i = 0; i< K - 1; i++)		//K - 1����ŭ ��� �̵�
				p = p.next;
			System.out.print(p.next.data);		//���� ����� next�� data�� ����Ʈ
			p.next = p.next.next;				//������� ���� ����
			arr.size--;							//size 1����
			if (arr.isEmpty())					//size == 0 �̸� ���� ��������
				break;
			System.out.print(", ");				//�������� �� �κ��� ��µǸ� �ȵ�
		}
		System.out.println(">");
	}
}

class Node{										//Node Ŭ����
	Node next;
	int data;
	Node(int data){
		this.data = data;
		this.next = null;
	}
}

class CircularLinkedList{						//���� ���Ḯ��Ʈ Ŭ����
	Node head;
	Node tail;
	int size = 0;
	public void add(int data) {					//add �Լ�
		Node newNode = new Node(data);
		if (head == null) {						//ó�� ���� �־��ִ� ���
			head = newNode;
			tail = newNode;
			this.head.next = this.tail;
			this.tail.next = this.head;
		}
		else {									//������ ���
			Node p = this.head;
			for (int i = 0; i < size - 1; i++)	//�������� ��尡 ����Ǿ��ֱ� ������ ���ѷ����� ������ �ʰ� size�� �̿��Ͽ� ��ȸ
				p = p.next;
			p.next = newNode;
			this.tail = newNode;
			this.tail.next = head;				//tail�� ����
		}
		this.size++;
	}
	public boolean isEmpty() {
		return this.size == 0;
	}
}
