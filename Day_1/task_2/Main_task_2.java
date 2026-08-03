class Main_task_2 {
    public static void main(String[] args) {
        System.out.println("Hello World");
        String [] str ={"task1","task2","task3","task4","task5"};
        stack_order stk=new stack_order();
        stk.st(str);
        queue_order que=new queue_order();
        System.out.println();
        que.qu(str);
        }
}
