package javapro.Enum;

public class enumt {
    public static void main(String[] args) {

        Weekday day = Weekday.SUN;
        if (day == Weekday.SUN) {
            System.out.println("Right!");
        }
    }
}

enum Weekday {
    SUN, MON, TUE, WED, THU, FRI, SAT;
}