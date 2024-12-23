package activities;

public class Activity12 {
	public static void main(String[] args) {
		Addable ad1=(num1,num2)->(num1+num2);
		System.out.println("Addition of num1,num2 is: "+ad1.add(1, 3));
		
		Addable ad2=(int num1,int num2)->{
			return(num1+num2);
		};
		System.out.println("Addition of num1,num2 is: "+ad2.add(10,30));
	}
}
