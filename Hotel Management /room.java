import java.io.Serializable;
import java.util.ArrayList;

class Food implements Serializable {
    int itemno;
    int quantity;
    float price;

    Food(int itemno, int quantity) {
        this.itemno = itemno;
        this.quantity = quantity;
        switch (itemno) {
            case 1:
                price = quantity * 50;
                break;
            case 2:
                price = quantity * 60;
                break;
            case 3:
                price = quantity * 70;
                break;
            case 4:
                price = quantity * 30;
                break;
        }
    }
}

class Singleroom implements Serializable {
    String name;
    String contact;
    String gender;
    ArrayList<Food> food = new ArrayList<>();

    Singleroom() {
        this.name = "";
    }

    Singleroom(String name, String contact, String gender) {
        this.name = name;
        this.contact = contact;
        this.gender = gender;
    }
    // Additional methods and logic for Singleroom if any
}

class Doubleroom extends Singleroom implements Serializable {
    String name2;
    String contact2;
    String gender2;

    Doubleroom() {
        super();
        this.name2 = "";
    }

    Doubleroom(String name, String contact, String gender, String name2, String contact2, String gender2) {
        super(name, contact, gender);
        this.name2 = name2;
        this.contact2 = contact2;
        this.gender2 = gender2;
    }
    // Additional methods and logic for Doubleroom if any
}
