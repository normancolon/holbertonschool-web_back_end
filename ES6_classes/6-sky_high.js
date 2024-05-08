// Import the Building class from '5-building.js'
import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // Call the constructor of the parent class (Building)
    this._floors = floors; // Initialize _floors with the floors argument
  }

  // Getter for sqft (inherited)
  get sqft() {
    return this._sqft;
  }

  // Getter for floors
  get floors() {
    return this._floors;
  }

  // Override the required abstract method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}

