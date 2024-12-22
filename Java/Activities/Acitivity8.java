package activities;

public class Acitivity8 {
	public static void main(String[] args) {
		MountainBike mb = new MountainBike(3,0,25);
		 System.out.println(mb.bicycleDesc());
		    mb.speedUp(20);
		    mb.applyBrake(5);
		    mb.setHeight(30);
	        
	        // Print the updated bicycle description
	        System.out.println(mb.bicycleDesc());
		}
	}
