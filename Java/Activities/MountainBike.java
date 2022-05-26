package activities;

public class MountainBike extends Bicycle {

    int seatHeight;

    public MountainBike(int gears, int speed, int height) {
        super(gears, speed);
        seatHeight = height;
    }

    public void setHeight(int newSeatHeight) {
        seatHeight = newSeatHeight;
    }

    public void bicycleDesc() {
        System.out.println("No. of Gears = " + gears + " and Current Speed = " + currentSpeed + " and Seat Height = " + seatHeight);
    }
}
