package activities;

public class Car {
    String color;
    String transmission;
    int make;
    int tyres;
    int doors;

    public Car() {
        this.tyres = 4;
        this.doors = 4;
    }

    void displayCharacteristics() {
        System.out.println("Car has following Characteristics");
        System.out.println("Color : " + color);
        System.out.println("Transmission : " + transmission);
        System.out.println("Make : " + color);
        System.out.println("No. Of Tyres : " + tyres);
        System.out.println("No. Of Doors : " + doors);

    }

    void accelerate() {
        System.out.println("Car is moving forward.");
    }

    void brake() {
        System.out.println("Car has stopped.");
    }
}