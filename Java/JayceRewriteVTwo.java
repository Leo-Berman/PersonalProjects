public class JayceRewriteVTwo {
  public static int Power(int A, int B, int C){
    if(B!=0) return Power(A,B-1,A*C);
    return C;
  }
  public static Boolean isCubed(int A, int B){
    // Find the power
    int a = Power(B,3,1);

    // Check to see if the test number is the actual number if so return true if not eh
    if(A==a){
      System.out.print(B);
      System.out.print("^3 is equal to");
      System.out.println(A);
      return true;
    }
    // Otherwise, check the next number and return false?? Idk what you're trying to do
    System.out.print(B);
    System.out.print("^3 is not equal to ");
    System.out.println(A);    
    return false;  
  }

  public static void main(String[] args){ // Rewrite working under the assumption you are trying to check if 5^3 - 125
    // checking if 5^3 = 125
    System.out.println(isCubed(125,5));

    // checking if 4^3 = 125
    System.out.println(isCubed(125, 4));
  }
}