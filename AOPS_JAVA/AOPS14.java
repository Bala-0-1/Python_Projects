package AOPS_JAVA;

public class AOPS14{
    public static void main(String[] args) {
        int[] arr = new int[]{1,2,1,3,2,1,4,5};
        AOPS14 ap = new AOPS14();
        // System.out.println(ap.removeDuplicates(arr));
    }

    public int multiplyAllListValues(int[] arr){
        int num = 1;
        for(int i:arr){
            num*=i;
        }
        return num;
    }

    // public int[] removeDuplicates(int[] arr){
        
    // }
}