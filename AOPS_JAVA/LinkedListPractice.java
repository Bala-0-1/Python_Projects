package AOPS_JAVA;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Vector;
import java.util.Iterator;
import java.util.concurrent.CopyOnWriteArrayList;

public class LinkedListPractice {

    public static void main(String[] args) {
        List<String> cc = new ArrayList<>();
        List<String> ls = new ArrayList<>();
        ls.add("Apple");
        ls.add("Orange");
        ls.add("Pineapple");
        MyIterator iter = new MyIterator(ls);
        while(iter.hasNext()){
            System.out.println(iter.next());
        }
        
    }

}

class MyIterator implements Iterator{
    private List<String> myList;
    private int currentPointer;


    MyIterator(List<String> myList){
        this.myList = myList;
        this.currentPointer = myList.size()-1;
    }

    @Override
    public boolean hasNext() {
        if(currentPointer >= 0){
            return true;
        }
        else{
            return false;
        }
    }

    @Override
    public Object next(){
        Object ob = myList.get(currentPointer);
        currentPointer--;
        return ob;    
    }
    
}