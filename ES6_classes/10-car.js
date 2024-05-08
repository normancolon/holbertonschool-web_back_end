/**
 * Represents a car with a brand, motor, and color.
 */
export default class Car {
    /**
     * Constructs a new Car instance.
     * @param {string} brand - The brand of the car.
     * @param {string} motor - The type of motor the car uses.
     * @param {string} color - The color of the car.
     */
    constructor(brand, motor, color) {
      if (typeof brand !== 'string' || !brand.trim()) {
        throw new Error('Brand must be a non-empty string');
      }
      if (typeof motor !== 'string' || !motor.trim()) {
        throw new Error('Motor must be a non-empty string');
      }
      if (typeof color !== 'string' || !color.trim()) {
        throw new Error('Color must be a non-empty string');
      }
      this._brand = brand;
      this._motor = motor;
      this._color = color;
    }
  
    /**
     * Allows setting and getting the constructor to use when cloning instances.
     */
    static get [Symbol.species]() {
      return this;
    }
  
    /**
     * Creates a new instance of the car with the same properties.
     * @returns {Car} A new instance of the car.
     */
    cloneCar() {
      const Species = this.constructor[Symbol.species];
      return new Species(this._brand, this._motor, this._color);
    }
  }
  