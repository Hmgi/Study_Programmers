package java;

import java.util.*;

public class Main_4108{
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        
        while(true){
            int y = sc.nextInt();
            int x = sc.nextInt();
            
            if(x == 0 && y == 0) return;

            char[][] arrs = new char[y][x];

            for(int i = 0; i < y; i++){
                arrs[i] = sc.next().toCharArray();
            }

            for(int i = 0; i < y; i++){
                for(int j = 0; j < x; j++){
                    if(arrs[i][j] != '*'){
                        arrs[i][j] = (char)(checkQ(arrs, i, j) + '0');
                    }
                }
                //System.out.println();
            }

            for(int i = 0; i < y; i++){
                for(int j = 0; j < x; j++){
                    System.out.print(arrs[i][j]);
                }
                System.out.println();
            }

            //System.out.println("arrs length : " + arrs[0].length);
            //System.out.println("arrs : " + arrs[2][1]);
        }
    }

    static int checkQ(char[][] arrs, int y, int x){
        int startx = (x - 1 < 0) ? 0 : x - 1;
        int starty  = (y - 1 < 0) ? 0 : y - 1;
        int endx  = (x + 1 == arrs[0].length) ? arrs[0].length - 1 : x + 1;
        int endy  = (y + 1 == arrs.length) ? arrs.length - 1 : y + 1;

        int count = 0;

        //System.out.println("x : " + x + "/ y : " + y + "/st : " + startx + "/ sy : " + starty + "/ ex : " + endx + "/ ey : " + endy);

        for(int i = starty; i <= endy; i++){
            for(int j = startx; j <= endx; j++){
                if(arrs[i][j] == '*') count++;
            }
        }
        //System.out.println("count : " + count);
        return count;
    } 
}