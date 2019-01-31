
import java.util.PropertyResourceBundle;
import jdk.nashorn.internal.ir.BreakNode;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Md Aiman Sharif
 */
public class Assignment1 {
   
   /**
    * Recursive method to choose k out of n things
    * @param n way to choose n things
    * @param k way to choose k things
    * @return the number of ways using recursion
    */
   public static int c(int n, int k){
      System.out.print("c(" + n + "," + k + ") " + "= " );
      if (k == n) { //checks whether k is equal to n base case
         System.out.println("1");
         return 1; //base case 
      }
      else if(k == 0){ //checks whether k is equal to 0 base case
         System.out.println("1");
         return 1;
      }
      else if (k > n) { //base case checks whether k > n
         System.out.println("c" + "(" + n + "," + k + ") = 0");
         return 0;
      } 
      System.out.println("c(" + (n-1) + "," + (k-1) + ") + " + "c(" + (n-1) + "," + (k) + ")");
      return c(n - 1, k - 1) + c(n - 1, k);
   }
   
   /**
    * Recursive method to calculate the number of ways to organize a parade
    * @param n length 
    * @return the number of ways a parade can be organized
    */
   public static int P(int n){
      if(n == 1) //base case
         return 2;
      else if(n == 2) //base case
         return 3;
      
      return P(n - 1) + P(n - 2); //returns the order of the parade recursively
   }
   
   /**
    * Recursive method to write a character repeatedly 
    * form a line of n characters
    * @param ch character to be written repeatedly
    * @param n number of characters to be written
    */
   public static void writeLine(char ch, int n){
      if(n == 1){ //base case
         System.out.print(ch); //prints out last character
      }
      
      else {
         System.out.print(ch); //prints out the character
         writeLine(ch, n - 1); //recursive call to the function
      }
   }
   
   /**
    * Recursive method to write m lines of characters each
    * @param ch number of characters to be written
    * @param n number of characters to be written
    * @param m number of lines of n characters each
    */
   public static void writeBlock(char ch, int n, int m){
      if(m == 1){ //base case
         writeLine(ch, n); //calls writeLine to print out one line
         System.out.println(); //prints out a line
      }
      else{
         writeBlock(ch, n, 1); //prints out the first line
         writeBlock(ch, n, m - 1); //recursive call to print out lines
      }
   }
   
   /**
    * Recursive method which reverses digits of a given number
    * @param number to be reversed 
    */
   public static void reverseDigits(int number){
      if(number < 10){ //base case
         System.out.println(number); //prints out last digit of reversed number
         return;
      }
      
      int numDigit = number % 10; //extract the last digit
      System.out.print(numDigit); //prints out the last digit
      
      reverseDigits(number / 10); //extract the remaining digits
   }
   
   /**
    * Searches the array from first to last for the value
    * if the value is in the array
    * method returns the index of the array item that equals value
    * @param anArray array to be searched in
    * @param first starts from this value
    * @param last ends searching at this value
    * @param value searches the array for this value
    * @return the index of the value in the array
    */
   public static int myBinarySearch(String [] anArray, int first, int last, String value){
      int arrayIndex; 
      
      if(first > last){
         arrayIndex = -1; //if value not found in array
      }
      else {
         int mid = (first + last) / 2; //mid value
         if (value.equals(anArray[mid])){
            arrayIndex = mid; //value is found at anArray[mid]
         }
         else{
            arrayIndex = myBinarySearch(anArray, mid + 1, last, value); 
            if(arrayIndex == -1)
               arrayIndex = myBinarySearch(anArray, first, mid - 1, value);
         }
      }
      return arrayIndex;
   }
   
   //Main method to test the methods with some test cases
   
   public static void main(String args[]){
      String array[] = new String[]{"cows", "sheep", "cats", "dogs", "fox"};
      
      System.out.println("Method 1 \n");
      System.out.println(c(3, 2));
      
      System.out.println("\nMethod 2");
      System.out.println(P(5) + "\n");
      
      System.out.println("Method 3");
      writeLine('*', 6);
      System.out.println("\n");
      
      System.out.println("Method 4");
      writeBlock('*', 4, 5);
      System.out.println();
      
      System.out.println("Method 5");
      reverseDigits(12345);
      System.out.println();
      
      
      System.out.println("Method 6\n");
      System.out.println("sheep: " + myBinarySearch(array, 0, 4, "sheep"));
      System.out.println("fox: " + myBinarySearch(array, 0, 4, "fox"));
   }
}
