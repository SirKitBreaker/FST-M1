package activities;

public class Activity7 {
    public static void main(String[] args) {
        MountainBike mb = new MountainBike(3, 0, 25);
        System.out.println("Initial State :");
        mb.bicycleDesc();

        mb.speedUp(20);
        System.out.println("After Speed Up :");
        mb.bicycleDesc();

        mb.applyBrake(5);
        System.out.println("After Applying Brake :");
        mb.bicycleDesc();
    }
}
