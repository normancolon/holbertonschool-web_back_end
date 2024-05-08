// 2-hbtn_course.js
export default class HolbertonCourse {
    constructor(name, length, students) {
      this.name = name;      // Using the setter to validate during assignment
      this.length = length;  // Using the setter to validate during assignment
      this.students = students;  // Using the setter to validate during assignment
    }
  
    // Getter for name
    get name() {
      return this._name;
    }
  
    // Setter for name
    set name(newName) {
      if (typeof newName !== 'string') throw new TypeError('Name must be a string');
      this._name = newName;
    }
  
    // Getter for length
    get length() {
      return this._length;
    }
  
    // Setter for length
    set length(newLength) {
      if (typeof newLength !== 'number') throw new TypeError('Length must be a number');
      this._length = newLength;
    }
  
    // Getter for students
    get students() {
      return this._students;
    }
  
    // Setter for students
    set students(newStudents) {
      if (!Array.isArray(newStudents) || newStudents.some(s => typeof s !== 'string')) {
        throw new TypeError('Students must be an array of strings');
      }
      this._students = newStudents;
    }
  }
  
  