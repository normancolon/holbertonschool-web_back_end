#!/usr/bin/node
export default class ClassRoom {
  /**
   * Constructs a ClassRoom with a specified maximum number of students.
   * @param {number} maxStudentsSize - Maximum number of students the classroom can accommodate.
   */
  constructor(maxStudentsSize) {
    if (typeof maxStudentsSize !== 'number') {
      throw new Error("Maximum students size must be a number");
    }
    this._maxStudentsSize = maxStudentsSize;
  }
}

