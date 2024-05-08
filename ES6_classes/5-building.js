// 5-building.js
export default class Building {
    constructor(sqft) {
      if (new.target === Building) {
        throw new Error('Building cannot be instantiated directly');
      }
      if (this.evacuationWarningMessage === undefined) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
      this._sqft = sqft;
    }
  
    // Getter for sqft
    get sqft() {
      return this._sqft;
    }
  }
  