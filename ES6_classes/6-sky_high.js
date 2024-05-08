// Assuming Building is correctly defined in 5-building.js and imported here.
import Building from './5-building';

/**
 * Represents a high-rise building with multiple floors.
 */
class SkyHighBuilding extends Building {
  /**
   * Constructs a new SkyHighBuilding instance.
   * @param {number} sqft The total square footage of the building.
   * @param {number} floors The number of floors in the building.
   */
  constructor(sqft, floors) {
    super(sqft);
    if (typeof floors !== 'number' || floors <= 0) {
      throw new Error("Floors must be a positive number.");
    }
    this._floors = floors;
  }

  /**
   * Retrieves the square footage of the building.
   * @return {number} The square footage.
   */
  get sqft() {
    return this._sqft;
  }

  /**
   * Retrieves the number of floors in the building.
   * @return {number} The number of floors.
   */
  get floors() {
    return this._floors;
  }

  /**
   * Provides a message detailing evacuation procedures, specifically noting the number of floors.
   * @return {string} The evacuation message.
   */
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}

export default SkyHighBuilding;
