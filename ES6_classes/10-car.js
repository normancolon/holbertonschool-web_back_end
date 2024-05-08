#!/usr/bin/node
export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Clone the car by creating a new instance of the current class
  cloneCar() {
    return new this.constructor(this._brand, this._motor, this._color);
  }
}
