/*
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
 */
public class Kata {
    public static int[] digitize(long n) {
        String stringN = String.valueOf(n);
        int numberOfDigits = stringN.length();
        int[] digitsArray = new int[numberOfDigits];
        for (int i = 0; i<numberOfDigits; i++){
            int letterIndex = numberOfDigits-1-i;
            digitsArray[i] = (stringN.charAt(letterIndex) - '0');
        }
        return digitsArray;
    }
}