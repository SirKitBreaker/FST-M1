package activities;


public class Bicycle implements BicycleParts, BicycleOperations {
    public int gears;
    public int currentSpeed;

    public Bicycle(int gears, int speed) {
        this.gears = gears;
        this.currentSpeed = speed;
    }

    public void applyBrake(int decrement) {

        currentSpeed = currentSpeed - decrement;

    }

    public void speedUp(int increment) {

        currentSpeed = currentSpeed + increment;

    }

    public void bicycleDesc() {
        System.out.println("No. of Gears = " + gears + " and Current Speed = " + currentSpeed);
    }
}
