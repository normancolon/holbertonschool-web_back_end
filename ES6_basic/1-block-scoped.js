export default function taskBlock(trueOrFalse) {
    let task = false;  // Using let for block scope
    let task2 = true;  // Using let for block scope
  
    if (trueOrFalse) {
      let task = true;  // This task is scoped only within this if block
      let task2 = false; // This task2 is scoped only within this if block
      console.log(task, task2); // Optional: to check values inside the block
    }
  
    return [task, task2];
  }
  