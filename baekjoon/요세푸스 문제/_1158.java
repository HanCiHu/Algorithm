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
		for (int i = 0; i < N; i++)				//원형 연결리스트값 초기화
			arr.add(i + 1);
		System.out.print("<");
		Node p = arr.tail;
		while(true) {
			for (int i = 0; i< K - 1; i++)		//K - 1번만큼 노드 이동
				p = p.next;
			System.out.print(p.next.data);		//현재 노드의 next의 data를 프린트
			p.next = p.next.next;				//출력해준 노드는 삭제
			arr.size--;							//size 1감소
			if (arr.isEmpty())					//size == 0 이면 루프 빠져나옴
				break;
			System.out.print(", ");				//마지막은 이 부분이 출력되면 안됨
		}
		System.out.println(">");
	}
}

class Node{										//Node 클래스
	Node next;
	int data;
	Node(int data){
		this.data = data;
		this.next = null;
	}
}

class CircularLinkedList{						//원형 연결리스트 클래스
	Node head;
	Node tail;
	int size = 0;
	public void add(int data) {					//add 함수
		Node newNode = new Node(data);
		if (head == null) {						//처음 값을 넣어주는 경우
			head = newNode;
			tail = newNode;
			this.head.next = this.tail;
			this.tail.next = this.head;
		}
		else {									//보통의 경우
			Node p = this.head;
			for (int i = 0; i < size - 1; i++)	//원형으로 노드가 연결되어있기 때문에 무한루프에 빠지지 않게 size를 이용하여 순회
				p = p.next;
			p.next = newNode;
			this.tail = newNode;
			this.tail.next = head;				//tail값 조정
		}
		this.size++;
	}
	public boolean isEmpty() {
		return this.size == 0;
	}
}
