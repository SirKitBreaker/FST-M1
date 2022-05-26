package activities;

public class Activity8 {

    public static void main(String[] args) {

        Activity8 Ex = new Activity8();
        try {
            Ex.exceptionTest("Test Exception using String");
            Ex.exceptionTest(null);
        } catch (CustomException e) {
            System.out.println("Error Message : " + e.getMessage());
        }


    }

    public void exceptionTest(String str) throws CustomException {
        if (str == null) {
            throw new CustomException("This is a Custom Error --> String is null");
        } else {
            System.out.println(str);
        }
    }
}
