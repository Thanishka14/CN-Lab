import java.util.Scanner;

class CharacterStuffing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter message: ");
        String msg = sc.nextLine();

        System.out.print("Enter flag: ");
        String flag = sc.nextLine();

        System.out.print("Enter escape: ");
        String esc = sc.nextLine();

        String s = msg.replace(esc, esc + esc);
        s = s.replace(flag, esc + flag);

        String stuffed = flag + s + flag;

        System.out.println("After stuffing: " + stuffed);

        String d = stuffed.substring(flag.length(),
                stuffed.length() - flag.length());

        d = d.replace(esc + flag, flag);
        d = d.replace(esc + esc, esc);

        System.out.println("After destuffing: " + d);

        sc.close();
    }
}
