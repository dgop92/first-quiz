package org.velezreyes.quiz.question6;

public class KarenTea implements Drink {

    /**
     * The price in cents
     */
    private int price = 100;

    public int getPrice() {
        return price;
    }

    @Override
    public String getName() {
        return "KarenTea";
    }

    @Override
    public boolean isFizzy() {
        return false;
    }

}
