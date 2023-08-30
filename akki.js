class Person {
    constructor(name = "Tom", age = 20, energy = 100) {
      this.name = name;
      this.age = age;
      this.energy = energy;
    }
  
    sleep() {
      this.energy += 10;
    }
  
    doSomethingFun() {
      this.energy -= 10;
    }
  }
  console.log(person); // Person { name: 'Tom', age: 20, energy: 100 }
person.sleep();
console.log(person.energy); // 110
person.doSomethingFun();
console.log(person.energy); // 100

///task 2

  class Worker extends Person {
    constructor(name = "Tom", age = 20, energy = 100, xp = 0, hourlyWage = 10) {
      super(name, age, energy);
      this.xp = xp;
      this.hourlyWage = hourlyWage;
    }
  
    goToWork() {
      this.xp += 10;
    }
  }

  console.log(worker); // Worker { name: 'Alice', age: 30, energy: 120, xp: 0, hourlyWage: 10 }
worker.goToWork();
console.log(worker.xp); // 10
  ///task 3

  function createIntern() {
    const intern = new Worker("Bob", 21, 110, 0, 10);
    intern.goToWork();
    return intern;
  }
  
  const internObject = createIntern();
  console.log(internObject);
  function createManager() {
    const manager = new Worker("Alice", 30, 120, 100, 30);
    manager.doSomethingFun();
    return manager;
  }
  
  const managerObject = createManager();
  console.log(managerObject);
  