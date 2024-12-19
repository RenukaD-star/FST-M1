package activities;
public class Activity2 {
	public static void main(String[] args) {
		//initialize an array
		int[] Arr= {10, 77, 10, 54, -11, 10};
		
		// length of array
		System.out.println(Arr.length);
		
		int sum = 0;
   
    for(int i=0;i<Arr.length;i++) {
    	if(Arr[i] == 10) {
    		sum= sum + Arr[i];	
    	}
    	
    }
    //print sum of 10's
    System.out.println("Totalsum of 10s in array:" + sum);
    
    // Result is True or False
    
    if (sum == 30) {
    	System.out.println("True");
    }
    else {
    	System.out.println("False");
    }
	}
}
    
    

