package activities;

import java.util.Arrays;

public class Activity4 {


    void SortArray(int[] numbers) {
        int temp;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                if (numbers[i] > numbers[j]) {
                    temp = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(numbers));

    }

    public static void main(String[] args) {
        int[] numbers = {4, 10, 3, 2, 5, 7, 6, 1, 9, 8};
        System.out.println(Arrays.toString(numbers));

        Activity4 Sort = new Activity4();
        Sort.SortArray(numbers);
    }


}
