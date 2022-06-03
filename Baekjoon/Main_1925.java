import java.util.*;

public class Main_1925{
    public static void main(String[] args)
    {

        Scanner sc = new Scanner(System.in);
        
        double x, y, z = 0;
        int x1 = sc.nextInt();
        int x2 = sc.nextInt();
        int y1 = sc.nextInt();
        int y2 = sc.nextInt();
        int z1 = sc.nextInt();
        int z2 = sc.nextInt();

        if((x2 - y2) * (y1 - z1) == (y2 - z2) *(x1 - y1)){
            System.out.println("X");
            return;
        }

        x = calcLength(x1, x2, y1, y2);
        y = calcLength(y1, y2, z1, z2);
        z = calcLength(z1, z2, x1, x2);

        findMax(x, y, z);
    }

    static double calcLength(int x1, int x2, int y1, int y2)
    {
        return Math.pow(y1 - x1, 2) + Math.pow(y2 - x2, 2);
    }

    static void findMax(double x, double y, double z)
    {
        if(x == y && y == z) System.out.println("JungTriangle");

        else if(x == y || y == z || x == z)
        {
            if(x >= y && x >= z) check2Q(x, y, z);
            else if(y >= x && y >= z) check2Q(y, x, z);
            else check2Q(z, x, y);
        }

        else
        {
            if(x >= y && x >= z) checkQ(x, y, z);
            else if(y >= x && y >= z) checkQ(y, x, z);
            else checkQ(z, x, y);
        }
        return;
    }

    static void check2Q(double max, double a, double b)
    {
        if(a + b == max) System.out.println("Jikkak2Triangle");
        else if(a +b < max) System.out.println("Dunkak2Triangle");
        else System.out.println("Yeahkak2Triangle");
        return;
    }

    static void checkQ(double max, double a, double b)
    {
        if(a + b == max) System.out.println("JikkakTriangle");
        else if(a +b < max) System.out.println("DunkakTriangle");
        else System.out.println("YeahkakTriangle");
        return;
    }
}