/**
 * Represents a class cohort at Holberton School.
 */
export class HolbertonClass {
  constructor(year, location) {
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

// Create instances of HolbertonClass for 2019 and 2020 cohorts.
const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

/**
 * Represents a student at Holberton School.
 */
export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get holbertonClass() {
    return this._holbertonClass;
  }

  // Returns a full description including the student's name, and their class year and location.
  get fullStudentDescription() {
    return `${this.fullName} - ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
  }
}

// Array of students for easy management and display.
const listOfStudents = [
  new StudentHolberton('Guillaume', 'Salva', class2020),
  new StudentHolberton('John', 'Doe', class2020),
  new StudentHolberton('Albert', 'Clinton', class2019),
  new StudentHolberton('Donald', 'Bush', class2019),
  new StudentHolberton('Jason', 'Sandler', class2019)
];

export default listOfStudents;

