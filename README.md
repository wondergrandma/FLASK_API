# Binary-Tree

### Obsahuje funkcie:

Pridanie prvkov. 

Funkcia na vypísanie hodnôt v poradí Preorder, ktorú je možne modifikovať prehodením riadkov vo funkcii, môže byť vytvorené poradie Inorder a Postorder.
```
private void printPreorder(Uzol uzol)
    {
        if(uzol != null)
        {
            System.out.print(" " + uzol.getData());
            printPreorder(uzol.getLeft());
            printPreorder(uzol.getRight());
        }
    }
```

Funkcia na nájdenie najmenšej hodnoty, ktorá môže byť modifikovaná na najväčšiu zmenou `getLeft` na `getRight`.
```
public int minValue(Uzol uzol)
    {
        Uzol tmp = uzol;
        while (tmp.getLeft() != null) {
            tmp = tmp.getLeft();
        }
        return (tmp.getData());
    }
```

Funkcia na porovnanie hĺbky stromu.
