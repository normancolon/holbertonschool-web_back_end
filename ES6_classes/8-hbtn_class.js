// 8-hbtn_class.js
export default class HolbertonClass {
    constructor(size, location) {
      this._size = size;     // Private-like property for size
      this._location = location; // Private-like property for location
    }
  
    // Getter for size
    get size() {
      return this._size;
    }
  
    // Setter for size
    set size(value) {
      if (typeof value !== 'number') throw new TypeError('Size must be a number');
      this._size = value;
    }
  
    // Getter for location
    get location() {
      return this._location;
    }
  
    // Setter for location
    set location(value) {
      if (typeof value !== 'string') throw new TypeError('Location must be a string');
      this._location = value;
    }
  
    // Override the valueOf method to allow numeric conversions
    valueOf() {
      return this.size;
    }
  
    // Override the toString method to allow string conversions
    toString() {
      return this.location;
    }
  }
  