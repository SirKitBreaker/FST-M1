package activities;

public class Activity6 {

    public static void main(String[] args) throws InterruptedException {

        Plane airIndia = new Plane(10);
        airIndia.onboard("Pooja");
        airIndia.onboard("Rahul");
        airIndia.onboard("Gaurav");
        airIndia.onboard("Rani");
        System.out.println("Time of Takeoff : " + airIndia.takeOff());
        System.out.println("List of Passengers : " + airIndia.getPassesngers());
        Thread.sleep(5000);
        airIndia.land();
        System.out.println("Time of Landing : " + airIndia.getLastTimeLanded());


    }
}
