package activities;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Activity13 {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<>();
        Random indexGen = new Random();
        System.out.println("Please enter some numbers.");
        System.out.println("To exit enter any character.");

        while (scan.hasNextInt()) {
            list.add(scan.nextInt());
        }

        Integer[] nums = list.toArray(new Integer[0]);
        int idx = indexGen.nextInt(nums.length);
        System.out.println("Index value generated: " + idx + " Corresponding Value : " + nums[idx]);
        scan.close();
    }
}
