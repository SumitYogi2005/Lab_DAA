public class Maintask1
 {
     public static void main(String[] args) {
        System.out.println("Hello World");
        int[] num={8,3,15,6,2};
        comparison c=new comparison();
        int max=c.compare(num);
        System.out.println("The maximum value is: " + max);
        sorting s= new sorting();
        s.sort(num);
        for(int i=0;i<num.length;i++){
                System.out.print(num[i]+" ");
        }
}
}
