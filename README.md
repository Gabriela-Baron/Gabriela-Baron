import java.util.Scanner; public

class EvenOdd {

    public static void main(String args []) {

        Scanner sn = new Scanner(System.in);

        int number;

        String result; 

        System.out.print("Type a int value: ");

        number = sn.nextInt();

        result = (number % 2 == 0) ? "even" : "odd";

        System.out.print(result);

    }

}
