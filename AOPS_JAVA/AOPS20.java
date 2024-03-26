package AOPS_JAVA;

// 1). Create a number list in python and multiply all numbers in the list and print the output.

// 2). Create a list of elements which contains duplicate elements also and remove all the duplicates in the list.

// 3). Create an array of 20 elements and insert an element in the 5th position such that the next elements are pushed down. Calculate the time complexity required for this code and show as output.

public class AOPS20 {
    public static void main(String[] args) {
        AOPS20 a = new AOPS20();
        int[] arr = new int[]{1,2,1,0,0,2,3,15,4,3,1,2,0};
        System.out.println(a.multiplyAllListValues(arr));
        a.display(a.removeDuplicates(arr));
        a.display(a.insertByIndex(arr,2,10));
    }

    public int multiplyAllListValues(int[] arr){
        int num = 1;
        for(int i:arr){
            num*=i;
        }
        return num;
    }

    public boolean exist(int[] arr ,int num){
        for(int i = 0 ;i<arr.length;i++){
            if(arr[i] == num){
                return true;
            }
        }
        return false;
    }

    public int[] removeDuplicates(int[] arr){
        int[] newArr = new int[arr.length];
        int count = 0;
        boolean isZero = true;
        for(int i = 0;i<arr.length;i++){
            if(isZero && arr[i] == 0){
                newArr[count] = arr[i];
                isZero = false;
                count+=1;
            }
            else if(!exist(newArr, arr[i])){
                newArr[count] = arr[i];
                count++;
            }
        }
        int[] returnArr = new int[count];
        for(int i =0 ;i<returnArr.length;i++){
            returnArr[i] = newArr[i];
        }

        return returnArr;
    }

    public int[] insertByIndex(int[] arr,int index, int val){
        int[] newArr = new int[arr.length+1];
        for(int i=0;i<index;i++){
            newArr[i] = arr[i];
        }
        newArr[index] = val;
        for(int i = index;i<newArr.length-1;i++){
            newArr[i+1] = arr[i];
        } 
        return newArr;
    }


    public void display(int[] arr){
        String str = "[";
        if(arr.length == 0){
            str = "[]";
        }
        else{
        for(int i = 0;i<arr.length;i++){
            if(i!=arr.length-1){
                str+=arr[i]+",";
            }
            else{
                str+=arr[i];
            }
        }
        str+="]";
    }
        System.out.println(str);
    }
}
