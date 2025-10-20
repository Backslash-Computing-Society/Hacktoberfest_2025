// Example of TypeScript with type annotations
const greeting: string = "Hello, World!";

class TypeScriptGreeter {
  constructor(private name: string = "World") {}

  public greet(): void {
    console.log(`Hello, ${this.name}!`);
  }
}

const greeter = new TypeScriptGreeter();
greeter.greet();
