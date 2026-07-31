

public class stack_order {
    public void st(String[]str ) {
        String [] stak=new String [str.length];
        int top=-1;
        for(int i=0;i<str.length;i++ ){
            top++;
            stak[top]=str[i];
        }
        //push the values 
        while(top>-1){
           // top--;
            System.out.print(stak[top]+" ");
            top--;
        }
    }
}
