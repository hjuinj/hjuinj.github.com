---
title: "C# and Windows Architecture"
author: "hjuinj"
date: "29 November 2015"
output: html_document
---

#Multi-dim Array
int[ , ] arrayName = new int[10,10];
#Jagged arrays
```{C#}
int[][] jaggedArray = new int[10][];
jaggedArray[0] = new Type[5]; // Can specify different sizes.
jaggedArray[1] = new Type[7];
//...
jaggedArray[9] = new Type[21];
```

# Enum
```{C#}
enum Day : short { Sunday = 1, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };
Day.Sunday
```
      
# Structs
Watch out for the access modifiers:
```{C#}
public struct Coffee
{
   // This is the custom constructor.
   public Coffee(int strength, string bean, string countryOfOrigin)
   {
      this.Strength = strength;
      this.Bean = bean;
      this.CountryOfOrigin = countryOfOrigin;
   }
  // These statements declare the struct fields and set the default values.
   public int Strength;
   public string Bean;
   public string CountryOfOrigin; 
   // Other methods, fields, properties, and events.
}
```
Properties and Indexers are worthwhile investigating into.



# Class
public partial class DrinksMachine
{

   public void MakeCappuccino()
   {
      // Method logic goes here.
   }
}


public partial class DrinksMachine
{

   public void MakeEspresso()
   {
      // Method logic goes here.
   }
}

### Partial Class
When working with automatically generated source. Visual Studio uses this approach when your application uses Windows Forms, Web service wrapper code, etc. Microsoft recommends that you do not modify the auto-generated code for these components as it could be overwritten when the application is compiled or the project files changed.  Instead, you can create another portion of the class, as a partial class with the same name, and make your additions and edits there.

// Instantiating a Class by Using Type Inference
var dm = new DrinksMachine();

# Network


#Abstract Class
An abstract method cannot exist in non-abstract class
An abstract method is not permitted to have any implementation, including curly braces
An abstract method signature must end in a semi-colon
An abstract method MUST be implemented in any sub class.  Failure to do so will generate a compiler warning in C#.


To implement multiple interfaces, you add a comma-separated list of the interfaces that you want to implement to your class declaration. Your class must implement every member of every interface you add to your class declaration.  The following example shows how to create a class that implements multiple interfaces:

// Declaring a Class that Implements Multiple Interfaces
public class Coffee: IBeverage, IInventoryItem
{
}


Unmanaged objects are those that are not .NET components such as a Microsoft Word object, a database connection, or a file resource.