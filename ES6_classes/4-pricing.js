// Import the Currency class from the '3-currency.js' file
import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;   // Using the setter to validate during assignment
    this.currency = currency;  // Using the setter to validate during assignment
  }

  // Getter for amount
  get amount() {
    return this._amount;
  }

  // Setter for amount
  set amount(newAmount) {
    if (typeof newAmount !== 'number') throw new TypeError('Amount must be a number');
    this._amount = newAmount;
  }

  // Getter for currency
  get currency() {
    return this._currency;
  }

  // Setter for currency
  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) throw new TypeError('Currency must be an instance of Currency');
    this._currency = newCurrency;
  }

  // Method to display formatted price
  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  // Static method to convert price
  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Both amount and conversion rate must be numbers');
    }
    return amount * conversionRate;
  }
}
