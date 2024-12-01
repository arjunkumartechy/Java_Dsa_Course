package Basics;
import java.util.Scanner;
public class SpiralPattern {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            System.out.println("Enter the value of n : ");
            int n = input.nextInt();
            for(int i = 1 ; i <= 2*n-1;i++){
                for(int j = 1 ; j <= 2*n-1; j++){
                    int topDist = i - 1 ;
                    int bottomDist = 2*n-1 - i ; 
                    int leftDist = 2*n-1 - j ; 
                    int rightDist = j - 1 ;
                    System.out.print(n-(Math.min(Math.min(topDist,bottomDist),Math.min(leftDist,rightDist)))+" "); 
                }
                System.out.println();
            } 
            int x = 10  ; // x is reference var in stack & 10 is the actual object stored in heap . x is pointing to 10  . 
            System.out.println(x);
            // More than one ref vars can point to same object. change via one     

        }
    }
}
