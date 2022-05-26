package activities;

import java.util.HashSet;

public class Activity10 {

    public static void main(String[] args) {
        HashSet hs = new HashSet();
        hs.add("Fruits");
        hs.add(1);
        hs.add("Colors");
        hs.add(254.05);
        hs.add("Garbage");
        hs.add("This is a String message");
        System.out.println("Initial HashSet: " + hs);
        System.out.println("Size of HashSet : " + hs.size());
        //remove true
        System.out.println("Removing Garbage : " + hs.remove("Garbage"));
        if (hs.remove(4)) {
            System.out.println("4 removed");
        } else {
            System.out.println("4 is not present, so cannot be removed");
        }
        System.out.println("Check if 1 exists in Hashset : " + hs.contains(1));
        System.out.println("Updated Hashset : " + hs);


    }
}
