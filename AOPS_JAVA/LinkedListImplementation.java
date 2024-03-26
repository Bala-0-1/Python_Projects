package AOPS_JAVA;

public class LinkedListImplementation {
	Node head;

    public void addNewNode(int data) {
        Node newNode = new Node(data, null);
        if(head == null){
            head = newNode;
        }else{
            Node temp = head;
            while(temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }
    public void deleteNodeAtIndex(int index) {
        int currIndex = 0;
        Node temp = head;
        Node prevNode=null, nextNode=null;
        if (index == 0 && temp.next != null) {
            nextNode = temp.next;
            head = nextNode;
        }else{
            while(currIndex < index) {
                prevNode = temp;
                nextNode = temp.next;
                temp = temp.next;
                currIndex = currIndex + 1;
            }
            prevNode.next = nextNode.next;
        }
        
    }
    public void deleteNode(int data) {
        Node temp = head;
        Node prevNode=null, nextNode;
        while(temp != null){
            nextNode = temp.next;
            if (temp.data == data) {
                if(prevNode == null) {
                    head = nextNode;
                }else{
                    prevNode.next =nextNode;
                }
                break;
            }
            prevNode = temp;
            temp = temp.next;
        }
    }
    public void updateLinkedList(int index, int data) {
        Node newNode = new Node(data, null);
        Node temp = head;
        int count = 0;
        Node prevNode = null;
        while(temp != null && count < index) {
            prevNode = temp;
            temp = temp.next;
            count = count + 1;
        }
        if(prevNode == null){
            Node nextNode = head;
            head = newNode;
            head.next = nextNode;
        }else{
            Node nextNode = prevNode.next;
            prevNode.next = newNode;
            newNode.next = nextNode;
        }
        
    }
    public void printLinkedList() {
        Node temp = head;
        while(temp != null){
            System.out.println(temp.data);
            temp = temp.next;
        }
    }

    public static void main(String[] args) {
        LinkedListImplementation ls = new LinkedListImplementation();

        ls.addNewNode(5);
        ls.addNewNode(10);
        ls.addNewNode(15);

        // ls.deleteNode(15);
        // ls.printLinkedList();

        ls.deleteNodeAtIndex(1);
        ls.updateLinkedList(0, 2);
        ls.updateLinkedList(2, 12);
        ls.printLinkedList();
    }
}

class Node{
    int data;
    Node next;

    Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }

}