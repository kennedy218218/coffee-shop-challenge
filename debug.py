from customer import Customer
from coffee import Coffee
from order import Order

def main():
    print("=== Welcome to the Coffee Shop Debug Demo ===")

    
    kennedy = Customer("Kennedy")
    kelvin = Customer("Kelvin")
    print(f"Customers created: {kennedy.name} and {kelvin.name}")

    
    Cappuccino = Coffee("Cappuccino")
    irish_coffee = Coffee("Irish Coffee")
    print(f"The following coffee varieties are available: {Cappuccino.name}, {irish_coffee.name}.")

    
    order1 = kennedy.create_order(Cappuccino, 4.75)
    order2 = kennedy.create_order(irish_coffee, 6.25)
    order3 = kelvin.create_order(Cappuccino, 5.50)

    print(f"{order1.customer.name} ordered a {order1.coffee.name} for ${order1.price}")
    print(f"{order2.customer.name} ordered a {order2.coffee.name} for ${order2.price}")
    print(f"{order3.customer.name} ordered a {order3.coffee.name} for ${order3.price}")

    
    print(f"\n{kennedy.name} has placed {len(kennedy.orders())} orders.")
    print(f"{kennedy.name} has ordered the following coffees: {[coffee.name for coffee in kennedy.coffees()]}")
    print(f"Buyers of {Cappuccino.name}: {[customer.name for customer in Cappuccino.customers()]}")
    print(f"Total purchases of {Cappuccino.name}: {Cappuccino.num_orders()}")

    print(f"\nAverage selling price of a {Cappuccino.name} is: ${Cappuccino.average_price():.2f}")
    print(f"{irish_coffee.name} has {irish_coffee.num_orders()} order(s).")

   
    aficionado = Customer.most_aficionado(Cappuccino)
    print(f"\nMost dedicated drinker of {Cappuccino.name}: {aficionado.name if aficionado else 'None'}")

    
    americano = Coffee("Americano")
    aficionado = Customer.most_aficionado(americano)
    print(f"Most dedicated drinker of {americano.name}: {aficionado.name if aficionado else 'None'}")

if __name__ == "__main__":
    main()


