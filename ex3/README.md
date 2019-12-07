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


Exercise 2: Inheritance
Step 1 :
Create two classes on separate files "car" and "bus", these classes can manage: - The registration of the vehicle
- The color of the vehicle
However each class has its specificities, the class car allows in addition to: - manage the number of doors of the car
The bus class allows you to:
- manage the number of floors of the bus
Be careful these two classes will inherit a common class that will allow them to share certain characteristics.
The number of floors and doors are values ​​that never change! A car can not have 1 door for example, likewise a 3-floor bus does not exist.
2nd step :
Create an instance of the bus class and the car class, give them the registration and the color of your choice. Indicate the number of floors of your choice for the bus and the number of doors of your choice for the car.
Step 3:
View the property values ​​for each vehicle in a row. Change the color of the car and the number of floors of the bus. Display attribute values ​​again
Do not forget to make sure that the values ​​for the number of doors and floors are the expected values. For example, I can not create a three-story bus. This will allow you to review encapsulation, getters and setters.