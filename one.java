class one
{
    public static void main(String[] args) {
        
        
Integer a = 1;
Integer b = 1;
System.out.println(a == b); // true, cached

Integer x = 1000;
Integer y = 1000;
System.out.println(x == y); // false, different objects

//System.out.println(x.equals(y)); // true, values are equal

    }
}