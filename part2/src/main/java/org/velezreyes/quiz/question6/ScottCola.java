package org.velezreyes.quiz.question6;

public class ScottCola implements Drink {

    /**
     * The price in cents
     */
    private int price = 75;

    public int getPrice() {
        return price;
    }

    @Override
    public String getName() {
        return "ScottCola";
    }

    @Override
    public boolean isFizzy() {
        return true;
    }

}
