// 3-currency.js
export default class Currency {
    constructor(code, name) {
      this.code = code;  // Using the setter to validate and assign value
      this.name = name;  // Using the setter to validate and assign value
    }
  
    // Getter for code
    get code() {
      return this._code;
    }
  
    // Setter for code
    set code(newCode) {
      if (typeof newCode !== 'string') throw new TypeError('Code must be a string');
      this._code = newCode;
    }
  
    // Getter for name
    get name() {
      return this._name;
    }
  
    // Setter for name
    set name(newName) {
      if (typeof newName !== 'string') throw new TypeError('Name must be a string');
      this._name = newName;
    }
  
    // Method to display name and code in the specified format
    displayFullCurrency() {
      return `${this.name} (${this.code})`;
    }
  }
  