Exercice 3 : Les méthodes magiques
Dans cet exercice nous allons simuler quelques comportements d’objets que nous pourrions retrouver dans la gestion d’un magasin.
Votre programme sera composé de deux classes principales : Customer et Employee. Toutes deux héritent d’une classe commune Person.
La classe personne définit les attributs nom, prénom et âge qui sont communs à la fois au client et à l’employé.
La classe client a comme attributs spécifiques un panier, vide par défaut, qui pourra contenir les produits que le client achète et un attribut avec le montant total à payer lors de son passage en caisse. Ce montant est mis à jour à chaque fois qu’un produit est ajouté au panier.
La classe employé possède quant à elle un attribut particulier, le statut du salarié. Par défaut celui-ci est employé. Les statuts possibles sont : employé, technicien, manager et cadre par ordre de hiérarchie.
Vous aurez également besoin de créer une classe Product qui représente les produits du magasin. Elle possède les attributs prix et nom du produit.
Vous pouvez maintenant instancier dans votre fichier main.py quelques produits factices, un client et un employé.
Cependant nous ne nous arrêtons pas en si bon chemin. Afin de faciliter l’utilisation de l’application, nous souhaitons modifier le comportement natif des classes Customer et Employee.
Pour la classe Customer, je dois pouvoir :
- Afficher une carte d’identité complète du client par un simple print. Autrement-dit, si j’ai une variable customer contenant une instance de la classe Customer je dois pouvoir écrire print(customer) et obtenir dans le terminal un petit texte affichant le nom, prénom et l’âge du client mais aussi le nom des produits qu’il a dans son panier et le montant à payer.
- Ajouter un produit au panier par une simple addition. Par exemple, si j’ai une variable customer représentant une instance de la classe Customer et une variable product représentant une instance de la classe Product, je dois pouvoir écrire customer + product. Le produit en question est alors ajouté au panier du client et le montant total à payer en caisse est mis à jour.
Pour la classe Employee, je dois pouvoir :
- Afficher une carte d’identité complète de l’employé par un simple print. Autrement-dit, si j’ai une variable employee contenant une instance de la classe Employee je dois pouvoir écrire print(employee) et obtenir dans le terminal un petit texte affichant le nom, prénom et l’âge de l’employé mais aussi sont statut.
- Vérifier que l’employé a le statut requis grâce à l’opérateur >=. Autrement-dit, si j’ai une variable employee contenant une instance de la classe Employee avec le statut ‘employee’ alors je dois pouvoir écrire print(employee >= ‘manager’) et cela affichera False dans la console. Inversement si j’écris print(employee >= ‘employee’) , cela doit afficher True dans la console.
Testez les comportements attendus dans le fichier main.py


Exercise 3: The magic methods
In this exercise we will simulate some object behaviors that we could find in the management of a store.
Your program will consist of two main classes: Customer and Employee. Both inherit a common class Person.
The person class defines the surname, first name, and age attributes that are common to both the customer and the employee.
The customer class has as specific attributes a basket, empty by default, which can contain the products that the customer buys and an attribute with the total amount to be paid at checkout. This amount is updated each time a product is added to the cart.
The class employed has a particular attribute, the status of the employee. By default this one is used. The possible statuses are: employee, technician, manager and manager in order of hierarchy.
You will also need to create a Product class that represents the products in the store. It has the price and product name attributes.
You can now instantiate in your main.py file some dummy products, a customer and an employee.
However we do not stop in this good way. In order to facilitate the use of the application, we want to modify the native behavior of the Customer and Employee classes.
For the Customer class, I must be able to:
- Display a complete identity card of the customer by a simple print. In other words, if I have a variable customer containing an instance of the class Customer I must be able to write print (customer) and get in the terminal a small text displaying the name, surname and age of the customer but also the name of the customer. products he has in his basket and the amount to pay.
- Add a product to the cart by a simple addition. For example, if I have a customer variable representing an instance of the Customer class and a product variable representing an instance of the Product class, I must be able to write customer + product. The product in question is then added to the customer's cart and the total amount payable at the checkout is updated.
For the Employee class, I must be able to:
- Display a full identity card of the employee by a simple print. In other words, if I have an employee variable that contains an instance of the Employee class, I must be able to write print (employee) and get a small text in the terminal that displays the surname, first name, and age of the employee, but also status.
- Check that the employee has the required status with the> = operator. In other words, if I have an employee variable containing an instance of the Employee class with the status 'employee' then I need to be able to write print (employee> = 'manager') and this will show False in the console. Conversely, if I write print (employee> = 'employee'), it should show True in the console.
Test the expected behaviors in the main.py file