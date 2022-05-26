package project;

public class Main
{
    public static void main(String[] args)
    {
        Strom s = new Strom();
        Uzol u = new Uzol();

        s.add(10);
        s.add(4);
        s.add(15);
        s.add(20);
        s.add(19);
        s.add(4);
        s.add(6);
        s.add(1);
        s.add(3);
        s.add(5);
        s.add(7);

        System.out.print("Preorder:");

        s.printPreorder();
        System.out.println();
        System.out.println();

        System.out.println("Najmenší prvok je: " + s.minValue(s.getRoot())+"\n");

        System.out.println("Najhlbší prvok je: " + s.deepestNode(s.getRoot())+"\n");

        if (s.check(s.getRoot()))
            System.out.println("Listy sú na rovnakej úrovni");
        else
            System.out.println("Listy nie su na rovnakej úrovni");





    }

}
