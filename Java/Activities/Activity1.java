package activities;

public class Activity1 {

    public static void main(String[] args) {

        Car audi = new Car();
        //assigning values to variable
        audi.make = 2014;
        audi.color = "Black";
        audi.transmission = "Manual";
        //calling functions
        audi.displayCharacteristics();
        audi.accelerate();
        audi.brake();
    }
}
