package activities;

public class Activity12 {

    public static void main(String[] args) {
        Addable ad1 = (a, b) -> (a + b);
        System.out.println("Lambda Expression Result : " + ad1.add(20, 40));
        Addable ad2 = (int a, int b) -> {
            return (a + b);
        };
        System.out.println("Lambda Function Result : " + ad2.add(55, 25));
    }

}
