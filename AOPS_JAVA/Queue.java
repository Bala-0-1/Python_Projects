package AOPS_JAVA;

import java.util.ArrayList;

public class Queue {
    ArrayList<QueueData> arr = new ArrayList<>();

    public void enqueue(String value){
        arr.add(new QueueData(value));
    }

    public void dequeue(){
        if(arr.size() != 0){
            arr.remove(0);
        }
        else{
            throw new RuntimeException("The array is empty!");
        }
    }
    @Override
    public String toString(){
        return arr.toString();
    }
}

class QueueData{
    String node;

    QueueData(){

    } 

    QueueData(String value){
        node = value;
    }
}