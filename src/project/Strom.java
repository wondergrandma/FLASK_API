package project;

public class Strom
{
    private Uzol root;

    public Uzol getRoot() {
        return root;
    }

    public void setRoot(Uzol root) {
        this.root = root;
    }

    public boolean isEmpty()
    {
        return root == null;
    }

    public void add(int vkladanaHodnota)
    {
        if(isEmpty())
        {
            // ak je strom prazdny prva vložená hodnota sa vloží na začiatok
            Uzol u = new Uzol();
            u.setData(vkladanaHodnota);
            root = u;
        }
        else
        {
            /*
            pozrieme sa či sa hodnota už neneachadza v strome
            ak sa nachádza do stromu sa nevloží
            ak sa nenachádza vloží sa nasledne podľa porovnania hodnôt
            na pravu alebo lavu stranu, podľa toho či je hodnota väčšia (pravá strana)
            alebo menšia (ľavá strana)
            */
            Uzol it = root;
            while(it != null)
            {
                if(it.getData() == vkladanaHodnota)
                {
                    return;
                }
                else if(vkladanaHodnota < it.getData())
                {
                    if(it.getLeft() == null/*pokial je voľné miesto môžeme vložiť hodnotu*/)
                    {
                        // vloží sa hodnota
                        Uzol u = new Uzol();
                        u.setData(vkladanaHodnota);
                        it.setLeft(u);
                    }
                    else
                    {
                        // posunieme ukazatel aby bolo možne vložiť novu hodnotu
                        it = it.getLeft();
                    }
                }
                else
                {
                    if(it.getRight() == null/*pokial je voľné miesto môžeme vložiť hodnotu*/)
                    {
                        // vloží sa hodnota
                        Uzol u = new Uzol();
                        u.setData(vkladanaHodnota);
                        it.setRight(u);
                    }
                    else
                    {
                        // posunieme ukazatel aby bolo možne vložiť novu hodnotu
                        it = it.getRight();
                    }
                }
            }
        }
    }

    //vypísanie položiek v poradi Preorder (root, left, right)
    public void printPreorder()
    {
        Uzol u = root;
        printPreorder(root);
    }

    private void printPreorder(Uzol uzol)
    {
        if(uzol != null)
        {
            System.out.print(" " + uzol.getData());
            printPreorder(uzol.getLeft());
            printPreorder(uzol.getRight());
        }
    }

    public int minValue(Uzol uzol)
    {
        Uzol tmp = uzol;

        //program prejde cez všetky ľavé hodnoty pokiaľ nenarazí na takú po ktorej nasleduje null
        // posledná lava hodnota je najmenšia
        while (tmp.getLeft() != null) {
            tmp = tmp.getLeft();
        }
        return (tmp.getData());
    }

    static int maxLevel = -1;
    static int res = -1;

    /*
    maxLevel - do premennej sa uklada zatial najnižšia navštívená hlbka
    res - do premennej sa uklada najhlbšia hodnota
    level - tu je uloženy root
    */

    static void find(Uzol root, int level)
    {
        if (root != null)
        {
            //level sa postupne zvyšuje
            find(root.getLeft(), ++level);

            if (level > maxLevel)
            {
                res = root.getData();
                maxLevel = level;
            }

            find(root.getRight(), level);
        }
    }

    public int deepestNode(Uzol root)
    {
        //vráti najhlbší uzol
        find(root, 0);
        return res;
    }

    int leafLevel = 0;
    boolean checkUtil(Uzol uzol, int level, int leafLevel)
    {
        if (uzol == null)
            return true;

        if (uzol.getLeft() == null && uzol.getRight() == null)
        {
            if (this.leafLevel == 0)
            {
                this.leafLevel = level;
                return true;
            }

            return (level == this.leafLevel);
        }

        return checkUtil(uzol.getLeft(), level + 1, this.leafLevel)
                && checkUtil(uzol.getRight(), level + 1, this.leafLevel);
    }

    boolean check(Uzol uzol)
    {
        //cez chceck utils porovname hlbky
        int level = 0;
        return checkUtil(uzol, level, leafLevel);
    }
}


