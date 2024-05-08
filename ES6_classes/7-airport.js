// 7-airport.js
export default class Airport {
    constructor(name, code) {
      this._name = name;  // Encapsulate name with an underscore prefix
      this._code = code;  // Encapsulate code with an underscore prefix
    }
  
    // Getter for name
    get name() {
      return this._name;
    }
  
    // Setter for name
    set name(value) {
      this._name = value;
    }
  
    // Getter for code
    get code() {
      return this._code;
    }
  
    // Setter for code
    set code(value) {
      this._code = value;
    }
  
    // Override toString method to customize object description
    toString() {
      return `[object ${this.code}]`;
    }
  }

  