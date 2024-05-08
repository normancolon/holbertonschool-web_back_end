/**
 * Represents an educational cohort at Holberton School.
 */
export class HolbertonClass {
    /**
     * Constructs a HolbertonClass with a year and location.
     * @param {number} year - The year the class started.
     * @param {string} location - The geographic location of the class.
     */
    constructor(year, location) {
      if (typeof year !== 'number') {
        throw new TypeError('Year must be a number');
      }
      if (typeof location !== 'string') {
        throw new TypeError('Location must be a string');
      }
      this._year = year;
      this._location = location;
    }
  
    get year() {
      return this._year;
    }
  
    get location() {
      return this._location;
    }
  }
  