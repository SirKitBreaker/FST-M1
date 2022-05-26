package activities;

import java.util.HashMap;

public class Activity11 {

    public static void main(String[] args) {

        HashMap<Integer, String> colours = new HashMap<Integer, String>();
        colours.put(1, "Black");
        colours.put(2, "Red");
        colours.put(4, "White");
        colours.put(5, "Yellow");
        colours.put(3, "Blue");
        System.out.println(colours);
        colours.remove(3);
        System.out.println("After removing Blue : " + colours);
        if (colours.containsValue("Green")) {
            System.out.println("Green color Exist");
        } else {
            System.out.println("Green color does not exist");
        }
        System.out.println("Size of HashMap : " + colours.size());

    }
}
