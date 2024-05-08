// Import the Building class from the module where it's defined
import Building from './5-building.js';

// Try to instantiate Building directly
try {
    const b = new Building(100);
} catch(err) {
    console.log(err.message);  // Should print error about direct instantiation
}

// Define a subclass without implementing the required method
class TestBuilding extends Building {}

// Attempt to instantiate the subclass without the required method
try {
    const testBuilding = new TestBuilding(200);
} catch(err) {
    console.log(err.message);  // Should print error about missing method
}

// Correctly implement a subclass with the required method
class ProperBuilding extends Building {
    evacuationWarningMessage() {
        return "Evacuate now!";
    }
}

// Attempt to instantiate the correctly implemented subclass
try {
    const properBuilding = new ProperBuilding(300);
    console.log(properBuilding.evacuationWarningMessage());  // Should not throw error
} catch(err) {
    console.log(err.message);
}
