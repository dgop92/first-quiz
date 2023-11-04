package org.velezreyes.quiz.question6;

/*
 * Considering that there is a getInstance method in the provided code, 
 * this is the singleton pattern
*/
public class VendingMachineImpl implements VendingMachine {

  private static VendingMachineImpl instance;
  /**
   * The current quantity is used to keep track of the cents inserted
   * in the current transaction. It is reduce based on the price of the drink
   */
  private int currentQuantity;
  /**
   * The total cents keeps track of the cents inserted in the machine
   * during its lifetime.
   */
  private int totalCents;

  /**
   * I will use a predefined list instead of allowing dynamic creation of
   * drinks. Also, I'm ignoring unique name validation for simplicity
   */
  private Drink[] drinks = {
      new ScottCola(),
      new KarenTea()
  };

  private VendingMachineImpl() {
    this.totalCents = 0;
    this.currentQuantity = 0;
  }

  public static VendingMachine getInstance() {
    if (instance == null) {
      instance = new VendingMachineImpl();
    }
    return instance;
  }

  @Override
  public void insertQuarter() {
    this.currentQuantity += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {

    Drink drink = null;

    for (Drink d : drinks) {
      if (d.getName().equals(name)) {
        drink = d;
        break;
      }
    }

    if (drink == null) {
      throw new UnknownDrinkException();
    }

    if (drink.getPrice() > this.currentQuantity) {
      throw new NotEnoughMoneyException();
    }

    // decrease the current cents quantity
    this.currentQuantity -= drink.getPrice();
    // increase the total cents quantity of the machine
    this.totalCents += drink.getPrice();

    return drink;
  }

  public int getTotalCents() {
    return this.totalCents;
  }

}