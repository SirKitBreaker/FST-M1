package activities;

import java.util.ArrayList;

public class Activity9 {

    public static void main(String[] args) {

        ArrayList<String> myList = new ArrayList<String>();
        myList.add("This");
        myList.add("is");
        myList.add("My");
        myList.add("List");
        myList.add("Hello");

        System.out.println("Objects in the List : ");
        for (String names : myList) {
            System.out.println(names);
        }

        System.out.println("Third Element in List is : " + myList.get(2));
        System.out.println("Check if Hello Exist in the list : ");
        if (myList.contains("Hello")) {
            System.out.println("Object Exist");
        } else {
            System.out.println("Object Does Not Exist");
        }
        System.out.println("Number of object in the list : " + myList.size());
        myList.remove("List");
        System.out.println("Number of object in the list after removal : " + myList.size());

    }

}
