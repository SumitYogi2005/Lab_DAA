//package Day_1.task_3;
class loop_test {
    
   public static void print_loop(int n){
        for (int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                System.out.print("*");
            }
            System.out.println();
        }
       // System.out.println("loop for x ='$n'");
    }
    public static void main(String [] args){
       int n=5;
       print_loop(n);
       n=10;
       print_loop(n);

    }
}
