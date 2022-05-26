package activities;

public class Activity3 {

    public static void main(String[] args) {
        double Seconds = 1000000000;
        double EarthSeconds = 31557600;
        double MercurySeconds = 0.2408467;
        double VenusSeconds = 0.61519726;
        double MarsSeconds = 1.8808158;
        double JupiterSeconds = 11.862615;
        double SaturnSeconds = 29.447498;
        double UranusSeconds = 84.016846;
        double NeptuneSeconds = 164.79132;
        double EarthYear = Seconds / EarthSeconds;

        System.out.println("Age on Earth : " + EarthYear);
        System.out.println("Age on Mercury : " + EarthYear / 0.2408467);
        System.out.println("Age on Venus : " + EarthYear / 0.61519726);
        System.out.println("Age on Mars : " + EarthYear / 1.8808158);
        System.out.println("Age on Jupiter : " + EarthYear / 11.862615);
        System.out.println("Age on Saturn : " + EarthYear / 29.447498);
        System.out.println("Age on Uranus : " + EarthYear / 84.016846);
        System.out.println("Age on Neptune : " + EarthYear / 164.79132);

    }
}
