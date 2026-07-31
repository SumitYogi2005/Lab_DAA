public class sorting {
    void mergesort(int[] arr,int h,int l){
        if(l>=h) return;
        int mid = l+(h-l)/2;
        mergesort(arr, l, mid);
        mergesort(arr, mid+1, h);
        merge(arr, l, h, mid);
    }
    void merge(int [] arr,int l, int h,int mid){
    int [] temp =new int [h-l+1];
    int i=l;
    int j=mid+1;
    int k=0;
    while(i<=mid && j<=h){
        if(arr[i]<=arr[j]){
            temp[k++]=arr[i++];
        }else{
            temp[k++]=arr[j++];
        }
    }
    while(i<=mid ){
        temp[k++]=arr[i++];
    }
    while(j<=mid){
        temp[k++]=arr[j++];
    }
    for(int x=0;x<temp.length;x++){
        arr[l+x]=temp[x];
    }
}
    public int[] sort(int []nums){
        //using merge sort 
        int h=nums.length-1;
        int l=0;
        mergesort(nums,h,l);
        return nums;
    }
    
}
