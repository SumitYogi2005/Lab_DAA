//package Day_1.task_2;

public class queue_order {
    public void qu(String[]str ) {
        String [] que=new String [str.length];
        int front=0;
        int rear=-1;
        for(int i=0;i<str.length;i++ ){
            rear++;
            que[rear]=str[i];
        }
        //push the values 
        while(front<=rear){
           // top--;
            System.out.print(que[front]+" ");
            front++;
        }
    } 
    
}
