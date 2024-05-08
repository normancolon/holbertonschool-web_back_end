// Importing the ClassRoom class from the '0-classroom.js' file
import ClassRoom from './0-classroom.js';

// Function to initialize an array of ClassRoom objects with specific sizes
function initializeRooms() {
  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34)
  ];
}

// Exporting the initializeRooms function so it can be imported and used in other files
export default initializeRooms;

