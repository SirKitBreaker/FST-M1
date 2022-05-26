package activities;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Plane {

    private List<String> passengers;
    private int maxPassengers;
    private Date lastTimeTookOf;
    private Date lastTimeLanded;

    Plane(int maxPassengers) {
        this.maxPassengers = maxPassengers;
        this.passengers = new ArrayList<String>();
    }

    public void onboard(String passenger) {
        //add passengers to the array using the add() method
        passengers.add(passenger);
    }

    public Date takeOff() {
        //returns the current date and time
        lastTimeTookOf = new Date();
        return lastTimeTookOf;
    }

    public void land() {
        //sets the value of lastTimeLanded to the current date and time. Also clear() the array.
        lastTimeLanded = new Date();
    }

    public Date getLastTimeLanded() {
        //returns the value of lastTimeLanded.
        return lastTimeLanded;
    }

    public List<String> getPassesngers() {
        //returns the array of passengers.
        return passengers;
    }
}
