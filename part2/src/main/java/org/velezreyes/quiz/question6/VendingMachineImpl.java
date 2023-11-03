package org.velezreyes.quiz.question6;

/*
 * Considering that there was a getInstance method in the provided code, 
 * this is the singleton pattern
*/
public class VendingMachineImpl implements VendingMachine {

  private static VendingMachineImpl instance;
  /*
   * The current quarter quantity is used to keep track of the quarters inserted
   * in the current transaction. It is reduce based on the price of the drink
   */
  private int currentQuarterQuantity;
  /*
   * The quarter quantity keeps track of the quarters inserted in the machine
   * during its lifetime. It is never reset
   */
  private int quarterQuantity;

  /*
   * I will use a predefined list instead of allowing dynamic creation of
   * drinks. Also. I'm ignoring the name validation for simplicity
   */
  private Drink[] drinks = {
      new ScottCola(),
      new KarenTea()
  };

  private VendingMachineImpl() {
    this.quarterQuantity = 0;
  }

  public static VendingMachine getInstance() {
    if (instance == null) {
      instance = new VendingMachineImpl();
    }
    return instance;
  }

  @Override
  public void insertQuarter() {
    this.quarterQuantity += 25;
    this.currentQuarterQuantity += 25;
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

    if (drink.getPrice() > this.currentQuarterQuantity) {
      throw new NotEnoughMoneyException();
    }

    // decrease the current quarter quantity
    this.currentQuarterQuantity -= drink.getPrice();
    // increase the quarter quantity using the price of the drink
    this.quarterQuantity += drink.getPrice();

    return drink;
  }

  public int getQuarterQuantity() {
    return this.quarterQuantity;
  }

}