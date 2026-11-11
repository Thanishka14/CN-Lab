import java.util.Scanner;

class BitStuffing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter binary message: ");
        String msg = sc.nextLine();

        String s = "";
        int count = 0;

        for (int i = 0; i < msg.length(); i++) {
            char ch = msg.charAt(i);
            s = s + ch;

            if (ch == '1') {
                count++;
                if (count == 5) {
                    s = s + "0";
                    count = 0;
                }
            } else {
                count = 0;
            }
        }

        System.out.println("After stuffing: " + s);

        String d = "";
        count = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            d = d + ch;

            if (ch == '1') {
                count++;
                if (count == 5) {
                    i++;
                    count = 0;
                }
            } else {
                count = 0;
            }
        }

        System.out.println("After destuffing: " + d);

        sc.close();
    }
}
