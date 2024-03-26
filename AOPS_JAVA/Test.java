package AOPS_JAVA;

import java.util.ArrayList;

public class Test {
    public static void main(String[] args) {
        ArrayList arr = new ArrayList<Integer>();
        arr.add(3);
        System.out.println(arr.remove(0));
    }


}
class Student{
    String name;
    public Student(){
        name = "";
    }
    public Student(String name){
        this.name = name;
    }
}