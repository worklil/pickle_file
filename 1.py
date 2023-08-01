import pickle

customer_data = []

pickle_customers = open('pickle_customers.pck','wb')

pickle.dump(customer_data,pickle_customers)

pickle_customers.close()

pickle_customers = open('liliia.pck','rb')

customer_data = pickle.load(pickle_customers)
pickle_customers.close()
print(customer_data)

customer_data.append('jjj')

pickle_customers = open('liliia.pck','wb')

pickle.dump(customer_data,pickle_customers)

pickle_customers.close()