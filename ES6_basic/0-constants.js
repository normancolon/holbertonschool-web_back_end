// Using const in taskFirst since the variable does not change
export function taskFirst() {
    const task = 'I prefer const when I can.';
    return task;
  }
  
  // Using let in taskNext since the variable 'combination' changes
  export function taskNext() {
    let combination = 'But sometimes let';
    combination += getLast();
  
    return combination;
  }
  
  // Assuming the function getLast() is exported and remains unchanged
  export function getLast() {
    return ' is okay';
  }
  