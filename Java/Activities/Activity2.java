package activities;

public class Activity2 {

    boolean CheckSum(int search_num, int[] numbers) {
        int sum = 0;
        for (int number : numbers) {

            if (number == search_num) {
                sum = sum + number;
            }
        }
        return (sum == 30);

    }

    public static void main(String[] args) {
        int[] numbers = {10, 77, 10, 54, -11, 10};
        int search_num = 10;
        Activity2 Check = new Activity2();
        System.out.println("Is Sum 30 ? - " + Check.CheckSum(search_num, numbers));
    }
}
